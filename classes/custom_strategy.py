
import pandas as pd
from typing import Optional

import MetaTrader5 as mt5
from backtesting import Strategy

class CustomStrategy(Strategy):

    def __init__(self, broker, data, params):
        super().__init__(broker, data, params)

        self.is_testing = True

    def set_live_params(self, *, symbol='', timeframe=mt5.TIMEFRAME_H1):
        self.is_testing = False
        self.symbol = symbol
        self.timeframe = timeframe

    def buy(self, *,
            size: float = 1.0,
            limit: Optional[float] = None,
            stop: Optional[float] = None,
            sl: Optional[float] = None,
            tp: Optional[float] = None,
            tag: object = None) -> 'Order':
        
        if self.is_testing:
            return super().buy(size=size, limit=limit, stop=stop, sl=sl, tp=tp, tag=tag)
        
        return self.open_position(mt5.ORDER_TYPE_BUY, size, sl, tp, 0, 0)

    def sell(self, *,
             size: float = 1.0,
             limit: Optional[float] = None,
             stop: Optional[float] = None,
             sl: Optional[float] = None,
             tp: Optional[float] = None,
             tag: object = None) -> 'Order':

        if self.is_testing:
            return super().sell(size=size, limit=limit, stop=stop, sl=sl, tp=tp, tag=tag)

        return self.open_position(mt5.ORDER_TYPE_SELL, size, sl, tp, 0, 0)

    def open_position(self, type, size, sl, tp, deviation, magic):
        
        request = self.get_request(type, size, sl, tp, deviation, magic)
        if request is None:
            return

        result = mt5.order_send(request)

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"order send failed with {result.retcode}")
            print(result)
            # return False
        else:
            print("we had success")
            print(result)

    def get_request(self, type, size, sl, tp, deviation, magic):

        # current price information
        price_info = mt5.symbol_info_tick(self.symbol)
        if price_info is None:
            print(f"Failed to get price information for {self.symbol}")
            return None
        
        if type == mt5.ORDER_TYPE_BUY:
            price = price_info.ask
            stop_loss_price = price_info.bid - sl
            take_profit_price = price_info.bid + tp
        else:
            price = price_info.bid
            stop_loss_price = price_info.ask + sl
            take_profit_price = price_info.ask - tp

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "magic": magic,
            "volume": size,
            "type": type,
            "price": price,
            "sl": stop_loss_price,
            "tp": take_profit_price,
            "deviation": deviation,
            "type_time": mt5.ORDER_TIME_GTC,
        }

        if not self.set_filling_mode(request):
            return None

        return request

    def set_filling_mode(self, request):

        for filling_mode in range(2):
            request['type_filling'] = filling_mode
            result = mt5.order_check(request)
            
            if result.comment == "Done":
                return True
        
        return False

    def get_rates_from_pos(self, symbol, timeframe, bar_count):

        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bar_count)        
        if rates is None:
            print('No rates data retrieved')
            return None

        rates_frame = pd.DataFrame(rates)
        rates_frame.rename(columns={'open':'Open', 'high':'High', 'low':'Low', 'close':'Close', 'tick_volume':'Volume'}, inplace=True)

        return rates_frame

    # common functions that will take different paths on test
    def get_open_trade_count(self, type):

        open_trades = 0

        if self.is_testing:
            if type==mt5.ORDER_TYPE_BUY:
                open_trades = sum(1 for trade in self.trades if trade.is_long)
            elif type==mt5.ORDER_TYPE_SELL:
                open_trades = sum(1 for trade in self.trades if trade.is_long)
            return open_trades
        
        positions = mt5.positions_get(symbol=self.symbol)

        if positions == None:
            return 0
        
        open_trades = sum(1 for position in positions if position['type']==type)
        return open_trades

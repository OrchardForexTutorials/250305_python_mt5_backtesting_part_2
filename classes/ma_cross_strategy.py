
import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta # take care with this

from backtesting._util import _Data
from classes.custom_backtesting import CustomStrategy

class MACrossStrategy(CustomStrategy):
    
    def init(self):

        self.fast_ma_period = 5
        self.slow_ma_period = 10

        self.lot_size = 0.1
        self.stop_loss_amount = 0.00100
        self.take_profit_amount = 0.00150

        self.buy_count = 0
        self.sell_count = 0

        # Calculate fast and slow moving averages
        if self.is_testing:
            self.fast_ma = self.I(SMA, self.data.Close, self.fast_ma_period)
            self.slow_ma = self.I(SMA, self.data.Close, self.slow_ma_period)

    def next(self):

        # get fresh data if in live mode
        if not self.is_testing:

            bar_count = self.fast_ma_period + self.slow_ma_period + 3
            rates = self.get_rates_from_pos(self.symbol, self.timeframe, bar_count)
            if rates is None:
                return
            
            self._data = _Data(rates.copy(deep=False))

            self.fast_ma = SMA(rates['Close'], self.fast_ma_period)
            self.slow_ma = SMA(rates['Close'], self.slow_ma_period)

        # Check for crossover
        if self.fast_ma[-1] < self.slow_ma[-1] and self.fast_ma[-2] >= self.slow_ma[-2]:

            # Fast MA crosses above Slow MA: Buy signal
            open_trades = self.get_open_trade_count(mt5.ORDER_TYPE_BUY)
            if open_trades > 0:
                return

            stop_loss_price = self.data.Close[-1]-self.stop_loss_amount
            take_profit_price = self.data.Close[-1]+self.take_profit_amount
            self.buy(size = self.lot_size, sl = stop_loss_price, tp = take_profit_price)
            self.buy_count += 1

        elif self.slow_ma[-1] < self.fast_ma[-1] and self.slow_ma[-2] >= self.fast_ma[-2]:

            # Slow MA crosses above Fast MA: Sell signal
            open_trades = self.get_open_trade_count(mt5.ORDER_TYPE_SELL)
            if open_trades > 0:
                return

            stop_loss_price = self.data.Close[-1]+self.stop_loss_amount
            take_profit_price = self.data.Close[-1]-self.take_profit_amount
            self.sell(size = self.lot_size, sl = stop_loss_price, tp = take_profit_price)
            self.sell_count += 1

# Define Simple Moving Average (SMA) function
def SMA(data, period):
    return ta.sma(pd.Series(data), length = period).to_numpy()

# pip uninstall pandas_ta
# pip install -U git+https://github.com/OrchardForexTutorials/pandas-ta.git --no-cache-dir

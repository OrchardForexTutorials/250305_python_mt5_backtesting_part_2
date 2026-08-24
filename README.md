# Python MT5 Backtesting Part 2

<!-- START_HEADER -->

<!-- END_HEADER -->

I'm taking a simple strategy and developing a structure where a Python trading robot can be backtested and run live on MetaTrader.

This is part of a series, and there is still more refinement to come. In the previous video, I showed how to run backtests on a strategy, but those backtests could only run in backtest mode. In this video, I modify the backtesting version so it can operate in both test and live modes.

The code is based on the previous version and is changed to use an MA cross trading robot. A custom backtesting class inherits from the existing backtest class and determines whether to use historical data for testing or execute live trading through MetaTrader 5.

The custom strategy class also supports both modes. In testing mode, it uses the existing backtesting functions. In live mode, it can execute buy and sell trades through MetaTrader 5, obtain current market data, count open positions, and calculate moving averages from recent rates.

The video also demonstrates using a forked version of pandas_ta to work around an incompatibility with NumPy 2 and later. This is a temporary workaround and should be replaced with the official version when the compatibility issue is resolved.

The code is still fairly rough and is intended as an intermediate step. Future improvements will make the structure cleaner and keep the differences between live and test processing out of the strategy code.

<!-- START_FOOTER -->

<!-- END_FOOTER -->
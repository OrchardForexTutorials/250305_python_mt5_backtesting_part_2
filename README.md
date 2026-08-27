# Python MT5 Backtesting Part 2

<!-- START_HEADER -->

Youtube:
{{VIDEO_DATA}}

For a broker with fast execution and tight spreads sign up to IC Markets using our affiliate link <br>
https://orchardforex.com/ic

<!-- END_HEADER -->

I'm taking a simple strategy and developing a structure where a Python trading robot can be backtested and run live on MetaTrader.

This is part of a series, and there is still more refinement to come. In the previous video, I showed how to run backtests on a strategy, but those backtests could only run in backtest mode. In this video, I modify the backtesting version so it can operate in both test and live modes.

The code is based on the previous version and is changed to use an MA cross trading robot. A custom backtesting class inherits from the existing backtest class and determines whether to use historical data for testing or execute live trading through MetaTrader 5.

The custom strategy class also supports both modes. In testing mode, it uses the existing backtesting functions. In live mode, it can execute buy and sell trades through MetaTrader 5, obtain current market data, count open positions, and calculate moving averages from recent rates.

The video also demonstrates using a forked version of pandas_ta to work around an incompatibility with NumPy 2 and later. This is a temporary workaround and should be replaced with the official version when the compatibility issue is resolved.

The code is still fairly rough and is intended as an intermediate step. Future improvements will make the structure cleaner and keep the differences between live and test processing out of the strategy code.

<!-- START_FOOTER -->
### Warning

This is not to be used for live trading

### License

The project is released under [GNU GPLv3 licence](https://www.gnu.org/licenses/quick-guide-gplv3.html),
so that means the software is copyrighted, however you have the freedom to use, change or share the software
for any purpose as long as the modified version stays free. See: [GNU FAQ](https://www.gnu.org/licenses/gpl-faq.html).

You should have received a copy of the GNU General Public License along with this program
(check the [LICENSE] file).
If not, please read <http://www.gnu.org/licenses/>.
For simplified version, please read <https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)>.

## Terms of Use

By using this software, you understand and agree that we (company and author)
are not be liable or responsible for any loss or damage due to any reason.
Although every attempt has been made to assure accuracy,
we do not give any express or implied warranty as to its accuracy.
We do not accept any liability for error or omission.

You acknowledge that you are familiar with these risks
and that you are solely responsible for the outcomes of your decisions.
We accept no liability whatsoever for any direct or consequential loss arising from the use of this product.
You understand and agree that past results are not necessarily indicative of future performance.

Use of this software serves as your acknowledgement and representation that you have read and understand
these TERMS OF USE and that you agree to be bound by such Terms of Use ("License Agreement").

### Copyright information

Copyright © 2013-2022 - Novateq Pty Ltd - All Rights Reserved

### Disclaimer and Risk Warnings

Trading any financial market involves risk.
All forms of trading carry a high level of risk so you should only speculate with money you can afford to lose.
You can lose more than your initial deposit and stake.
Please ensure your chosen method matches your investment objectives,
familiarize yourself with the risks involved and if necessary seek independent advice.

NFA and CTFC Required Disclaimers:
Trading in the Foreign Exchange market as well as in Futures Market and Options or in the Stock Market
is a challenging opportunity where above average returns are available for educated and experienced investors
who are willing to take above average risk.
However, before deciding to participate in Foreign Exchange (FX) trading or in Trading Futures, Options or stocks,
you should carefully consider your investment objectives, level of experience and risk appetite.
**Do not invest money you cannot afford to lose**.

CFTC RULE 4.41 - HYPOTHETICAL OR SIMULATED PERFORMANCE RESULTS HAVE CERTAIN LIMITATIONS.
UNLIKE AN ACTUAL PERFORMANCE RECORD, SIMULATED RESULTS DO NOT REPRESENT ACTUAL TRADING.
ALSO, SINCE THE TRADES HAVE NOT BEEN EXECUTED, THE RESULTS MAY HAVE UNDER-OR-OVER COMPENSATED FOR THE IMPACT,
IF ANY, OF CERTAIN MARKET FACTORS, SUCH AS LACK OF LIQUIDITY. SIMULATED TRADING PROGRAMS IN GENERAL
ARE ALSO SUBJECT TO THE FACT THAT THEY ARE DESIGNED WITH THE BENEFIT OF HINDSIGHT.
NO REPRESENTATION IS BEING MADE THAN ANY ACCOUNT WILL OR IS LIKELY TO ACHIEVE PROFIT OR LOSSES SIMILAR TO THOSE SHOWN.
<!-- END_FOOTER -->
import pandas as pd
import os

from backtesting import Strategy
from backtesting.lib import crossover
from talib import abstract
import talib

def MACD(values, fastperiod=12, slowperiod=26, signalperiod=9):
    TA_MACD = abstract.MACD
    return TA_MACD(values, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)[0]

def MACD_SIG(values, fastperiod=12, slowperiod=26, signalperiod=9):
    TA_MACD = abstract.MACD
    return TA_MACD(values, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)[1]

class MACDCross(Strategy):
    fastperiod = 12
    slowperiod = 26
    signalperiod = 9

    def init(self):
        # Precompute the two moving averages

        self.sma1 = self.I(MACD, self.data.Close, self.fastperiod, self.slowperiod, self.signalperiod)
        self.sma2 = self.I(MACD_SIG, self.data.Close,self.fastperiod, self.slowperiod, self.signalperiod)

    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

    def __str__(self):
        return f"MACD {self.fastperiod}, {self.slowperiod}, {self.signalperiod}"


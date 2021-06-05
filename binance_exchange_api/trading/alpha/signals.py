import os
import pandas as pd
from talib import abstract

def BBAND(values):
    BBANDS = abstract.BBANDS
    upperband, middleband, lowerband = BBANDS(values, timeperiod=20, nbdevup=2.0, nbdevdn=2.0, matype=0)
    return upperband, middleband, lowerband

def MACD(values):
    MACD = abstract.MACD
    macd, macd_sig, macd_graph = MACD(values )
    return macd, macd_sig, macd_graph

def RSI(values):
    RSI = abstract.RSI
    rsi = RSI(values)
    return rsi

def SMA(values, n):
    SMA = abstract.SMA
    sma_res = SMA(values,timeperiod=int(n) )
    return sma_res

def cross_over(series1,series2):
    sma_cros = series1[-2] < series2[-2] \
               and series1[-1] > series2[-1]
    return sma_cros
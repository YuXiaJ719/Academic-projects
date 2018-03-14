#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ Author: yuxia
@ Email: xiayu940179@gmail.com

Defining the functions used to calculate different technical indicators 
which will be used as training features.
"""

import numpy as np

path = './stocks data/StocksData.pickle'

return_period = 1
label_return_period = 5
rolling_day = 30
annualized_return = 0.08
threshold = annualized_return /(365 / label_return_period)

# exponiential moving average of return
def EMA(ret, days):
    ret = ret.values
    beta = 1 - 1 / days
    n = len(ret)
    ema = np.zeros(n)
    
    for i in range(n):
        if i == 0:
            ema[i] = ret[i]
        else:
            ema[i] = (beta * ema[i - 1] + (1 - beta)*ret[i])
            
    return ema

# Volume Ratio
def Volume_Ratio(volume, d):
    n = volume.shape[0]
    vr = np.zeros(n)
    
    for i in range(n):
        if i <= d:
            vr[i] = np.sum(volume.values[:i] > volume.values[i]) / np.sum(volume.values[:i+1] <= volume.values[i])
        else:
            vr[i] = np.sum(volume.values[i-d+1:i] > volume.values[i]) / np.sum(volume.values[i-d+1:i+1] <= volume.values[i])
    
    return vr

# BollingerBands
def BollingerBands(close, d):
    ma = close.rolling(window=d).mean()
    std = close.rolling(window=d).std()
    
    return ma + 2 * std, ma - 2 * std

# AroonIndex
def AroonIndex(close, d):
    close = close.values
    n = len(close)
    aroon_up = np.empty(n)
    aroon_down = np.empty(n)
    
    for ind in range(n):
        if ind <= d:
            aroon_up = (ind - np.argmax(close[:ind+1])) / (ind + 1) * 100
            aroon_down = (ind - np.argmin(close[:ind+1])) / (ind + 1) * 100
        else:
            aroon_up = (d - np.argmax(close[ind - d + 1:ind] + 1)) / d * 100
            aroon_down = (d - np.argmin(close[ind - d + 1:ind + 1])) / d * 100
                          
    return aroon_up, aroon_down
    
# Integrating all functions and return the dataframe
def createData(df):
    return_period = 1
    label_return_period = 5
    rolling_day = 30
    annualized_return = 0.08
    threshold = annualized_return /(365 / label_return_period)
    
    df.dropna(how="any", axis=0, inplace=True)
    df.set_index("Date", drop=True, inplace=True)
    
    df["Return"] = df["Close"].pct_change(periods=return_period)
    df["MeanReturn"] = df["Return"].rolling(window=rolling_day).mean()
    df["STD"] = df["Return"].rolling(window=rolling_day).std()
    df["d-Day-SharpeRatio"] = df["MeanReturn"] / df["STD"]
    df["VolumeRatio"] = Volume_Ratio(df["Volume"], rolling_day)
    df["10DayMean"] = df["Close"].rolling(window=10).mean()
    df["20DayMean"] = df["Close"].rolling(window=20).mean()
    df["40DayMean"] = df["Close"].rolling(window=40).mean()
    df["BBUP"], df["BBDN"] = BollingerBands(df["Close"], rolling_day)
    df["AroonUp"], df["AroonDown"] = AroonIndex(df["Close"], rolling_day)
    
    df.dropna(how="any", axis=0, inplace=True)
    
    df["EMA 12"] = EMA(df["Return"], 12)
    df["EMA 26"] = EMA(df["Return"], 26)
    df["Label"] = (df["Close"].pct_change(label_return_period).fillna(0).values > threshold) + 0
    df = df.iloc[label_return_period:]
    
    return df

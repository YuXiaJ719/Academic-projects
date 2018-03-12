#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ author: yuxia
@ Email: xiayu940719@gmail.com
"""

import time
import pickle
import os
import pandas_datareader as reader
from datetime import datetime


def retrive_data(stock_name, start, end, source="yahoo"):
    
    print("Collecting {}.".format(stock_name))
    
    for i in range(10):
        try:
            df = reader.DataReader(stock_name, source, start, end)
            break
        except:
            time.sleep(1)
            continue
    
    return df


if __name__ == "__main__":    
    with open('s&p500tickerscode.pickle', 'rb') as f:
        tickers = pickle.load(f)

    #Collect data from 01/01/2000 to now
    start = datetime(2000, 1, 1)
    end = datetime.now().date()
    
   #Initialize a dictionary to store stock data
    stocks_data = {}
    
    #Collect stock data and save as .csv file
    for stock_name in tickers:
        if(os.path.exists('./Data/' + stock_name + '.csv') != True):
            data = retrive_data(stock_name, start, end)
            data.to_csv('./Data/' + stock_name + '.csv')
            stocks_data[stock_name] = data
    
    #Save all stocks data in one file for easilt access
    with open('StocksData.pickle', 'wb') as f:
        pickle.dump(stocks_data, f)

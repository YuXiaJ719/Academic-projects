#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ author: yuxia
@ Email: xiayu940719@gmail.com
"""

import bs4 as bs
import requests
import pickle

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

def collect_tickers_code():
    response = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies', headers=headers)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    
    table = soup.find("table", {"class": "wikitable sortable"})
    tickers = []
    
    for row in table.findAll('tr')[1:]:
        tickers.append(row.findAll('td')[0].text.replace(".", "-"))
        
    with open('s&p500tickerscode.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    
#    print(tickers)
    
    return None
    

if __name__ == "__main__":
    collect_tickers_code()
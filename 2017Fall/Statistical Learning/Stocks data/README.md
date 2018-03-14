# Required libraries:
  - requests
  - bs4
  - pickle
  - pandas_datareader (version == 0.5.0)
  - datetime
  
Running "StockNames.py" will automatically collect s&p 500 tickers' codes and saved it in "s&p500tickerscode.pickle" in current directory.
  
Running "StockData.py" will load a list contains ticker names and automatically get transaction data from "yahoo finace", then store data below the directory named "./Data/ ", at last, stocks data will be dump to a file named "StocksData.pickle"below current directory.

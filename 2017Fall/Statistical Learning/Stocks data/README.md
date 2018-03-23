# Required libraries:
  - requests
  - bs4
  - pickle
  - pandas_datareader (version == 0.5.0)
  - datetime
  
Running "StockNames.py" will automatically collect s&p 500 tickers' codes and save it in "s&p500tickerscode.pickle" in current directory.
  
Running "StockData.py" will load a list which contains ticker names and automatically get transaction data from "yahoo finace", then put data into "./Data/ ". For convenience, stocks data will be dump into a .pickle file in current directory.

# Required libraries:
  - requests
  - bs4
  - pickle
  - pandas_datareader (version == 0.5.0)
  - datetime
  
Running "StockNames.py" will automatically collect s&p 500 tickers' codes and saved it in "s&p500tickerscode.pickle" in current directory.
  
Running "StockData.py" will load a list contains ticker names and automatically get transaction data from "yahoo finace", then put data into the directory named "./Data/ ". For convenience, stocks data will be dump to a .pickle file in current directory.

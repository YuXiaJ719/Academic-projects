import pickle
import datetime
import xgboost as xgb
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from DataProcessor import createData, createBackTestData

def update_estimator(data, stock_code, today):
    
    df_model = createData(data)
    features = df_model.values[:, :-1]
    label = df_model.values[:, -1]
    
    xgbc = xgb.XGBClassifier(max_depth=6, n_estimators=300, learning_rate=0.15)
    xgbc.fit(features, label)
    
    with open("./estimators/estimator_{}_{}.pickle".format(stock_code, today), "wb") as f:
        pickle.dump(xgbc, f)
        
def signal(data, stock_code, today):

    with open("./estimators/estimator_{}_{}.pickle".format(stock_code, today), "rb") as f:
        xgbc = pickle.load(f)
    
    df_pred = createBackTestData(data)
    prediction = xgbc.predict(df_pred.iloc[-1].values.reshape(1, -1))
    
    with open("./Tracking files/tracking_{}.txt".format(stock_code), "a") as f:
        f.write(str(today) + ": " + str(prediction[0]) + "\n")
        
def run(stock_code):
    
    today = datetime.datetime.now().date()
    size = datetime.timedelta(days=4000)
    start = today - size
    
    for i in range(10):
        try:
            data = pdr.DataReader(stock_code, "yahoo", start, today)
            break;
        except Exception as e:
            print(e)
            
    update_estimator(data, stock_code, today)
    signal(data, stock_code, today)
# Adding libraries and installed packages to requirements.txt:
# pip freeze > requirements.txt

# import numpy 
# import scipy 
# import pandas as pd 
# # import statsmodel 
# import pyfolio 


import pandas as pd 

# For price data 
import yfinance as yf 
from yahoofinancials import YahooFinancials


# General packages 



# Adding functions so code is easier to use: 


#getData calls the library and gets the data
# history is a pandas dataframe object
def getData(stockName):
    try:
        st = yf.Ticker(stockName)
        history = st.history(period="max", interval="1d")
    except Exception:
        print("Exception: " + Exception)


    return history


# useData gets complete dataframe from getData and only keeps close price and volume

def useData(history):
    try:
        df = history[["Close", "Volume"]]
    except Exception:
        print("Could not get data: " + Exception)
    print(df.head())
    

if __name__ == "__main__":
    df = getData("MSFT")
    useData(df)
    





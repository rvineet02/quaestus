# Adding libraries and installed packages to requirements.txt:
# pip freeze > requirements.txt

# import numpy 
# import scipy 
# import pandas as pd 
# # import statsmodel 
# import pyfolio 

import datetime 
import pandas as pd 

# For price data 
import yfinance as yf 
from yahoofinancials import YahooFinancials
from yfinance.utils import auto_adjust


# Functions from talib_functions.py for testing 
from talib_functions import TalibRSI



#getData calls the library and gets the data
# history is a pandas dataframe object
def getData(stockName):
    try:
        st = yf.Ticker(stockName)
        history = st.history(period="max", interval="1d")
    except Exception:
        print("Exception: " + Exception)

    # print(history.columns)

    return history


# useData gets complete dataframe from getData and only keeps close price and volume

def useData(history):
    try:
        df = history[["Close", "Volume"]]
    except Exception:
        print("Could not get data: " + Exception)

    return df 


def RSI(df):
    # Difference in price from previous day
    price = df["Close"]
    delta = price.diff()
    delta = delta[1:]

    # Series for Up (positive gains) and Down (negative gains)
    up, down = delta.clip(lower=0), -1*delta.clip(upper=0)

    # Calculate the Exponentially Weighted Moving Average 
    emp_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()

    rs = emp_up/ema_down
    
    rsi = 100 - (100/(1+rs))

    return rsi




if __name__ == "__main__":
    df = useData(getData("MSFT"))

    compareRSI()

# Adding libraries and installed packages to requirements.txt:
# pip freeze > requirements.txt

# import numpy 
# import scipy 
# import pandas as pd 
# # import statsmodel 
# import pyfolio 

import datetime 
import talib
import pandas as pd 

# For price data 
import yfinance as yf 
from yahoofinancials import YahooFinancials
from yfinance.utils import auto_adjust


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



# Only have this here to test my own written method
def TechRSI(df):
    close = df["Close"]
    rsi = talib.RSI(close, timeperiod=14)    
    return rsi


def compareRSI():

    mine = RSI(useData(getData("MSFT")))
    mine.sort_index(inplace=True)
    tlb = TechRSI(useData(getData("MSFT")))
    # tlb starts one extra day in 1986 so removing it
    tlb = tlb[1:]
    tlb.sort_index(inplace=True)

    # Making the two Series into one df to see values side-by-side    
    df = pd.concat([mine, tlb], axis=1)
    print(df.tail())

    # Prints true or false value by value keeping the index 
    # print(mine != tlb.values)


if __name__ == "__main__":
    df = useData(getData("MSFT"))

    # in_time_my_rsi = datetime.datetime.now()
    # RSI(df)
    # out_time_my_rsi = datetime.datetime.now()
    # print("Time taken for my RSI method: " + str(out_time_my_rsi - in_time_my_rsi))
    # in_time_import_rsi = datetime.datetime.now()
    # TechRSI(df)
    # out_time_import_rsi = datetime.datetime.now()
    # print("Time taken for imported RSI method: " + str(out_time_import_rsi - in_time_import_rsi)) 


    compareRSI()




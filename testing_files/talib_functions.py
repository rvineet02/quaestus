import talib
import testing_libs
import pandas as pd 
import numpy as np 
import tulipy as ti



# pandas Dataframe settings
# pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
# pd.reset_option('display.float_format')





# Only have this here to test my own written method
def TalibRSI(df):
    close = df["Adj Close"]
    rsi = talib.RSI(close, timeperiod=14)    
    return rsi


# Need to fix the SettingWithCopyWarning Error
# Fix this tomorrow
def movingAverages(df):
    df.loc["SMA_10"] = talib.MA(df["Adj Close"], timeperiod=10)
    # df["SMA_50"] = talib.MA(df["Adj Close"], timeperiod=50)
    # df["SMA_100"] = talib.MA(df["Adj Close"], timeperiod=100)
    # df["SMA_200"] = talib.MA(df["Adj Close"], timeperiod=200)

    # print(df.iloc[-2])
    # print(df.notna().idxmax())
    # print(df)


    print(df.tail())

def ti_SMA(df): 

    # print((ti.sma(df["Close"].values, period=9)).size)
    # df["SMA_9"] = ti.sma(df["Close"].values, period=5)


    arr9 = ti.sma(df["Adj Close"].values, period=10)
    print("10Day SMA: ", arr9[-2])
    # print("Size of df: ", df.shape)
    arr20 = ti.sma(df["Adj Close"].values, period=50)
    print("50D SMA: ", arr20[-2])


    # print(df.loc["2021-03-15"])
    # print(df)
    # print(df.notna())



if __name__ == "__main__":
    movingAverages(df=testing_libs.useData(testing_libs.secondSource("MSFT")))

    # ti_SMA(df=testing_libs.useData(testing_libs.secondSource("MSFT")))




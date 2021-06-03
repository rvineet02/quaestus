import talib
import getting_data as gd
import numpy as np 
import pandas as pd 


# Pandas dataframe settiongs
pd.set_option('display.float_format', lambda x: '%.5f' % x)
# to reset that option: 
# pd.reset_option('display.float_format')
# Set all values to five decimal places instead of scientific notation

# Supressing SettingWithCopyWarning Message: REVISE LATER
pd.options.mode.chained_assignment = None  # default='warn'


def CCI(df):
    data = df[["High", "Low", "Adj Close"]]
    commodity = talib.CCI(data["High"], data["Low"], data["Adj Close"], timeperiod=14)
    df["CCI"] = pd.Series(commodity, index=df.index)

    return df

def WilliamsR(df):
    data = df[["High", "Low", "Adj Close"]] 
    williams = talib.WILLR(data["High"], data["Low"], data["Adj Close"], timeperiod=14)
    df["WilliamsR"] = pd.Series(williams, index=df.index)
    
    
    return df

def RSI(df):
    data = df["Adj Close"]
    rsi = talib.RSI(data, timeperiod=14)
    df["RSI"] = pd.Series(rsi, index=df.index)

    print(df)

def StochRSI(df):
    data = df["Adj Close"]
    fastk, fastd = talib.STOCHRSI(data, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    df["StochRSI_fastk"] = pd.Series(fastk, index=df.index)
    df["StochRSI_fastd"] = pd.Series(fastd, index=df.index)
    
    
    return df



if __name__ == "__main__":
    StochRSI(df=gd.getData("TSLA"))



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


def ADX(df):
    data = df[["High", "Low", "Adj Close"]]
    adx = talib.ADX(data["High"], data["Low"], data["Adj Close"], timeperiod=14)
    df["ADX"] = pd.Series(adx, index=df.index)

    return df

def MACD(df):
    data = df["Adj Close"]
    macd, macdsignal, macdhist = talib.MACD(data, fastperiod=12, slowperiod=26, signalperiod=9)
    df["MACD"] = pd.Series(macd, index=df.index)

    return df


def ATR(df):
    data = df[["High", "Low", "Adj Close"]] 
    atr = talib.ATR(data["High"], data["Low"], data["Adj Close"], timeperiod=14)
    df["ATR"] = pd.Series(atr, index=df.index)

    return df

if __name__ == "__main__":
    ATR(df=gd.getData("TSLA"))

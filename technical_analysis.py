import talib
import getting_data as gd 
import numpy as np 
import pandas as pd 

# Pandas dataframe settiongs
# Set all values to five decimal places instead of scientific notation
pd.set_option('display.float_format', lambda x: '%.5f' % x)
# to reset that option: 
# pd.reset_option('display.float_format')


def SimpleMovingAverages(df):
    
    closing_prices = df["Adj Close"]

    moving_average = talib.MA(closing_prices, timeperiod=10, matype=0)
    df["MA_10"] = pd.Series(moving_average, index=df.index)

    print(df)


if __name__ == "__main__":
    SimpleMovingAverages(df=gd.getData("TSLA"))

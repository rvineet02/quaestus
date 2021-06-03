import talib
import getting_data as gd 
import numpy as np 
import pandas as pd 

# Pandas dataframe settiongs
pd.set_option('display.float_format', lambda x: '%.5f' % x)
# to reset that option: 
# pd.reset_option('display.float_format')
# Set all values to five decimal places instead of scientific notation


def SimpleMovingAverages(df):
    
    closing_prices = df["Adj Close"]    
    periods = [10, 50, 100, 200]
    for period in periods:
        moving_average = talib.MA(closing_prices, timeperiod=period, matype=0)
        df["MA_"+str(period)] = pd.Series(moving_average, index=df.index)

    print(df)


if __name__ == "__main__":
    SimpleMovingAverages(df=gd.getData("TSLA"))

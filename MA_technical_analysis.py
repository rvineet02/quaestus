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


def SimpleMovingAverages(df):
    
    closing_prices = df["Adj Close"]    
    periods = [10, 50, 100, 200]
    for period in periods:
        moving_average = talib.MA(closing_prices, timeperiod=period, matype=0)
        df["MA_"+str(period)] = pd.Series(moving_average, index=df.index)

    return df


def SimpleMovingAveragesCrossovers(df):
    df["Signal_10_50"] = 0.0
    df["Signal_50_100"] = 0.0
    df["Signal_100_200"] = 0.0    

    # Signal has value of 1 when shorter term MA > longer term MA 
    # Position finds the daily change in value of Signal
    # So if position is 1 it is a buy call since it moved from 0 to 1 
    # else if position is -1 it is a sell call since it moved from 1 to 0


    df['Signal_10_50'][10:] = np.where(df['MA_10'][10:] > df['MA_50'][10:], 1.0, 0.0)
    df['Signal_50_100'][50:] = np.where(df['MA_50'][50:] > df['MA_100'][50:], 1.0, 0.0)
    df['Signal_100_200'][100:] = np.where(df['MA_100'][100:] > df['MA_200'][100:], 1.0, 0.0)

    df["Position_10_50"] = df["Signal_10_50"].diff()
    df["Position_50_100"] = df["Signal_50_100"].diff()
    df["Position_100_200"] = df["Signal_100_200"].diff()

    
    # print(df.loc[df["Position_100_200"] == 1])
    
    print(df)


if __name__ == "__main__":
    print(SimpleMovingAverages(df=gd.getData("TSLA")))
    # SimpleMovingAveragesCrossovers(df=SimpleMovingAverages(df=gd.getData("TSLA")))


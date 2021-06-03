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

    return df


def SimpleMovingAveragesCrossovers(df):
    

    # Signal has value of 1 when shorter term MA > longer term MA 
    # Position finds the daily change in value of Signal
    # So if position is 1 it is a buy call since it moved from 0 to 1 
    # else if position is -1 it is a sell call since it moved from 1 to 0
    # short_term = [10,50,100]
    # long_term = [50,100,200]

    # for i in range(len(short_term)):
    #     df["Signal_"+str(short_term[i])+str(long_term[i])] = 0.0
    #     df["Signal_"+str(short_term[i])+str(long_term[i])][short_term[i]] = np.where(df["MA_"+str(short_term[i])][short_term[i]] > df["MA_"+str(long_term[i])][short_term[i]])

    df['Signal'][10:] = np.where(df['MA_10'][10:] > df['MA_50'][10:], 1.0, 0.0)
    df["Position"] = df["Signal"].diff()

    # print(df.loc[df["Position"] == 1])
    print(df)


if __name__ == "__main__":
    # SimpleMovingAverages(df=gd.getData("TSLA"))
    SimpleMovingAveragesCrossovers(df=SimpleMovingAverages(df=gd.getData("TSLA")))


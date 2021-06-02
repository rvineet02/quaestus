import talib

# Only have this here to test my own written method
def TalibRSI(df):
    close = df["Close"]
    rsi = talib.RSI(close, timeperiod=14)    
    return rsi



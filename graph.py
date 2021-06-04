from getting_data import getData
import pandas as pd 
import numpy as np 
import MA_technical_analysis as ma 
import Momentum_technical_analysis as mm
import getting_data as gd
import seaborn as sb
import matplotlib.pyplot as plt 


def graphSMA(df):
    plt.figure(figsize=[15,10])
    plt.grid(True)
    print("Working on it")
    plt.plot(df["Adj Close"], label="price")
    plt.plot(df["MA_10"], label="10D")
    plt.plot(df["MA_50"], label="50D") 
    plt.plot(df["MA_100"], label="100D")
    plt.plot(df["MA_200"], label="200D")
    plt.legend(loc=2)
    plt.show()



def graphRSI(df):
    # print(df.columns)
    # plt.grid(True)
    # Setting up two grids: one below the other
    fig1, ax = plt.subplots(2, sharex=True)
    # Plotting prices
    ax[0].plot(df["Adj Close"])
    ax[0].legend(loc="upper left")
    # Plotting RSI
    ax[1].plot(df["RSI"], color='green')
    ax[1].legend(loc="upper left")
    # Plotting lines at 30 and 70 (boundaries for overbought and oversold)
    ax[1].axhline(30, color='r', linestyle='--')
    ax[1].axhline(70, color='r', linestyle='--') 
    ax[1].axhspan(30, 70,color='b',alpha=.5)
    # General Plot stuff
    plt.suptitle("RSI and Stock Price")
    plt.show()

if __name__ == "__main__":
    # graphSMA(df=ma.SimpleMovingAverages(df=gd.getData("TSLA")))
    graphRSI(df=mm.RSI(df=gd.getData("TSLA")))

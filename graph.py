from getting_data import getData
import pandas as pd 
import numpy as np 
import MA_technical_analysis as ma 
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

if __name__ == "__main__":
    graphSMA(df=ma.SimpleMovingAverages(df=gd.getData("TSLA")))

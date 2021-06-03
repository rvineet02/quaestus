# Updated file to get data

from dataclasses import dataclass
import pandas as pd 
import yfinance as yf 
import datetime


def getData(ticker):
    try:
        stock = yf.download(ticker)
    except Exception:
        print("Could not getData()")
    return stock



# if __name__ == "__main__":
#     getData("TSLA")

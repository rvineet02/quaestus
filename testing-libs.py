# Adding libraries and installed packages to requirements.txt:
# pip freeze > requirements.txt

# General packages 
# import numpy 
# import scipy 
# import pandas as pd 
# # import statsmodel 
# import pyfolio 


# For price data 
import yfinance as yf 
from yahoofinancials import YahooFinancials



# Use of yf to get stock price information
tsla_info = yf.download('TSLA', start='2019-12-31',end='2020-01-01',progress=False)
print(tsla_info.head())





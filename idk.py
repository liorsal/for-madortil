import yfinance as yf
import pandas as pd

# Define the stock symbol and fetch historical data for the last 2 years with daily intervals
stock_symbol = 'AAPL'
stock_data = yf.download(stock_symbol, period='2y', interval='1d')

# Print the first few rows of the stock data
print(stock_data.head())

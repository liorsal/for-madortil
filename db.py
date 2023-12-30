import yfinance as yf
import pandas as pd

# Define the stock symbol
stock_symbol = 'AAPL'  # Replace with the desired stock symbol

# Fetch historical data for the last 5 days with a 5-minute interval
stock_data = yf.download(stock_symbol, period='1d', interval='5m')

# Convert the index (Datetime) to a column
stock_data.reset_index(inplace=True)

# Separate 'Date' and 'Time' from the 'Datetime' column
stock_data['Date'] = stock_data['Datetime'].dt.date
stock_data['Time'] = stock_data['Datetime'].dt.time

# Drop the original 'Datetime' column
stock_data.drop(columns=['Datetime'], inplace=True)

# Select the desired columns
selected_columns = ['Date', 'Time', 'Open', 'High', 'Low', 'Adj Close', 'Close', 'Volume']

# Keep only the last 5 rows
stock_data = stock_data.tail(5)

# Now you have the 'Date' and 'Time' columns separated and only the last 5 rows
stock_data = stock_data[selected_columns]

# Assuming you have a DataFrame called 'df'

# Get the last 5 rows of the DataFrame
last_5_rows = stock_data.tail(5)

# 'df' now contains only the last 5 rows of the original data
stock_data = stock_data.copy()

# Print the last 5 rows of the data
print(stock_data)

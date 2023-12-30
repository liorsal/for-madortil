import yfinance as yf
import pandas as pd

# Define the stock symbol
symbol = 'PLTR'

# Get current date and time
now = pd.Timestamp.now()

# Subtract 1 day from the current date to get yesterday's date
yesterday = now - pd.DateOffset(days=1)

# Determine the end date (last trading day) based on yesterday's date
end_date = yesterday.date()

# Generate date range with 5-minute frequency for yesterday's trading day
start_date = pd.Timestamp(f'{end_date} 09:30:00')
end_date = pd.Timestamp(f'{end_date} 16:00:00')
date_range = pd.date_range(start=start_date, end=end_date, freq='5min')

# Fetch stock data from Yahoo Finance with 5-minute interval
stock_data = yf.download(symbol, start=start_date, end=end_date, interval='5m')

# Filter stock data for the generated date range
df = stock_data[stock_data.index.isin(date_range)]

# Add 'Date' column as a separate column in the DataFrame
df['Date'] = df.index

# Reorder columns to have 'Date' as the first column
df = df[['Date'] + df.columns[:-1].tolist()]

# Write stock data to a CSV file
df.to_csv('pltr_stock_data.csv', index=False)

print(f'Stock data for {symbol} on yesterday\'s trading day has been saved to pltr_stock_data.csv')

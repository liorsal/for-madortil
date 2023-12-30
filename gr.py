import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and fetch historical data
stock_symbol = 'AAPL'  # Replace with the desired stock symbol
stock_data = yf.download(stock_symbol, period='1y')

# Extract Date and Close Price data
dates = stock_data.index
prices = stock_data['Close']

# Create a line graph
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, label=f'{stock_symbol} Closing Prices', color='blue')
plt.title(f'{stock_symbol} Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the graph
plt.tight_layout()
plt.show()

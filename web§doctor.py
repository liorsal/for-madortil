import yfinance as yf

# Define the stock symbol
stock_symbol = 'AAPL'  # Replace with the desired stock symbol

# Create a Ticker object
stock = yf.Ticker(stock_symbol)

# Fetch specific fundamental financial information
fundamentals = stock.info
selected_keys = [
    'earningsGrowth',
    'revenueGrowth',
    'freeCashflow',
    'returnOnAssets',
    'debtToEquity',
    'numberOfAnalystOpinions',
    'currentPrice',
    'targetHighPrice',
    'targetLowPrice',
    'targetMeanPrice',
    'targetMedianPrice'
]

# Display the selected fundamental information
for key in selected_keys:
    if key in fundamentals:
        print(f"{key}: {fundamentals[key]}")
    else:
        print(f"{key} not available for {stock_symbol}")

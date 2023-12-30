import sqlite3
import requests
from datetime import datetime
import time 
# Define API parameters
symbol = 'AAPL'
api_key = 'YOUR_API_KEY'
url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

# Connect to database and create table if it does not exist
conn = sqlite3.connect('pltr_stock_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stock_prices
             (timestamp TEXT, symbol TEXT, price REAL)''')

while True:
    try:
        # Retrieve data from API
        response = requests.get(url)
        response.raise_for_status()  # check if the response was successful
        data = response.json()

        # Parse data and store in database
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        price = float(data['Global Quote']['05. price'])
        c.execute("INSERT INTO stock_prices (timestamp, symbol, price) VALUES (?, ?, ?)", (timestamp, symbol, price))
        conn.commit()
        
        # Wait for 1 minute before retrieving the next data
        time.sleep(60)

    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
    except (KeyError, ValueError) as e:
        print(f'Parsing response failed: {e}')

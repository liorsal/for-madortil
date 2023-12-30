import requests
import pandas as pd
import time

url = 'https://www.alphavantage.co/query'
params = {
    'function': 'GLOBAL_QUOTE',
    'symbol': 'BTC',
    'apikey': '81BQVMEEQ91C0WOY'
}

dfs = []  # create an empty list to store the DataFrames

for i in range(15):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # check if the response was successful
        data = response.json()
        timestamp = pd.Timestamp.now().round('min')  # current timestamp rounded to minute
        price = float(data['Global Quote']['05. price'])  # current PLTR stock price in USD
        df = pd.DataFrame({
            'Open': [price],
            'High': [price],
            'Low': [price],
            'Adj': [price],
            'Close': [price],
            'Volume': [price]
        }, index=[timestamp])
        dfs.append(df)  # append the DataFrame to the list
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
    except (KeyError, ValueError) as e:
        print(f'Parsing response failed: {e}')
    
    time.sleep(60)  # wait for 1 minute before running the loop again

df = pd.concat(dfs)  # concatenate all the DataFrames in the list into a single DataFrame
print(df)

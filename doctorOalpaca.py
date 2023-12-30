import pandas as pd
import tkinter as tk
import numpy as np
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import pandas_ta as ta
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as si
import snscrape.modules.twitter as snt
from datetime import date, timedelta, timezone, datetime
from math import isnan
import sys
import alpaca_trade_api as tradeapi
import time
import requests
url = 'https://www.alphavantage.co/query'
params = {
    'function': 'GLOBAL_QUOTE',
    'symbol': 'PLTR',
    'apikey': '81BQVMEEQ91C0WOY'
}

dfs = []  # create an empty list to store the DataFrames

for i in range(30):
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

df = pd.concat(dfs)  # concatenate all the DataFrames in the list into a single DataFrame
output =  "hello \n" 
######################################bull patters start######################################################################
# Head and Shoulders Pattern Detection
# Define your data, e.g., a pandas DataFrame
data = df 
# Define parameters
left_shoulder_lookback = 20
head_lookback = 20
right_shoulder_lookback = 20
tolerance_percentage = 3

# Initialize pattern detection
head_and_shoulders_detected = False

# Loop through the data
for i in range(left_shoulder_lookback, len(data)-right_shoulder_lookback):
    
    # Check for potential left shoulder
    if data['High'][i] > data['High'][i-1] and data['High'][i] > data['High'][i+1]:
        
        # Check for potential head
        if data['High'][i] > data['High'][i-head_lookback:i].max() and data['High'][i] > data['High'][i+1:i+1+right_shoulder_lookback].max():
            
            # Check for potential right shoulder
            if data['High'][i] > data['High'][i+1] and data['High'][i] > data['High'][i+2]:
                
                # Check for neckline
                neckline = 0.5 * (data['Low'][i-head_lookback:i].min() + data['Low'][i+1:i+1+right_shoulder_lookback].min())
                
                # Check for confirmation
                if data['Low'][i] < neckline and data['Low'][i+1] < neckline and data['Low'][i+2] < neckline:
                    head_and_shoulders_detected = True
                    output += f"Head and Shoulders pattern detected at date: {data['Date'][i]}"

# Check for tolerance percentage
if not head_and_shoulders_detected:
    left_shoulder_lookback_with_tolerance = int(left_shoulder_lookback * (1 + tolerance_percentage/100))
    right_shoulder_lookback_with_tolerance = int(right_shoulder_lookback * (1 + tolerance_percentage/100))
    for i in range(left_shoulder_lookback_with_tolerance, len(data)-right_shoulder_lookback_with_tolerance):
        # Same logic as befo    re, but with tolerance percentage applied for lookback windows
        if data['High'][i] > data['High'][i-1] and data['High'][i] > data['High'][i+1] and data['High'][i-1] > data['High'][i-2] and data['High'][i+1] > data['High'][i+2]:
            head_and_shoulders_detected = True
            output += f"Head and Shoulders pattern detected at date: {data['Date'][i]} \n"
            break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

if len([c for c in output if c.isalpha()]) > 5:
    print(output)
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Identify Double Bottom pattern
double_bottom = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Close'][i-1] and data['Close'][i] < data['Close'][i+1]:
        double_bottom = True
        output += f"Double Bottom pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

# Identify Cup & Handle pattern
cup_and_handle = False
for i in range(2, len(data)-2):
    if data['Close'][i] < data['Close'][i-1] and data['Close'][i-1] < data['Close'][i-2] and data['Close'][i] < data['Close'][i+1] and data['Close'][i+1] < data['Close'][i+2]:
        cup_and_handle = True
        output += f"Cup & Handle pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Doji Pattern
doji = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]):
        doji = True
        output += f"Doji pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Hammer Pattern
hammer = False
for i in range(len(data)):
    if data['Close'][i] > data['Open'][i] and (data['High'][i] - data['Low'][i]) > 3 * (data['Open'][i] - data['Close'][i]) and (data['Close'][i] - data['Low'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        hammer = True
        output += f"Hammer pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Engulfing Pattern
bullish_engulfing = False
for i in range(1, len(data)-1):
    if data['Close'][i-1] < data['Open'][i-1] and data['Open'][i] < data['Close'][i] and data['Close'][i-1] < data['Open'][i] and data['Open'][i] < data['Close'][i-1] and (data['Close'][i] - data['Open'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        bullish_engulfing = True
        output += f"Bullish Engulfing pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Hammer Pattern
bullish_hammer = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]) and data['Close'][i] > data['Open'][i] and (data['Close'][i] - data['Low'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        bullish_hammer = True
        output += f"Bullish Hammer pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Harami Pattern
bullish_harami = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Open'][i] and data['Open'][i] < data['Close'][i-1] and data['Close'][i] > data['Open'][i-1] and data['Open'][i] < data['Close'][i-1]:
        bullish_harami = True
        output += f"Bullish Harami pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_inverted_hammer = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]) and data['Close'][i] > data['Open'][i] and (data['High'][i] - data['Close'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        bullish_inverted_hammer = True
        output += f"Bullish Inverted Hammer pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Morning Star Pattern
bullish_morning_star = False
for i in range(2, len(data)-2):
    if data['Close'][i-2] < data['Open'][i-2] and data['Close'][i-1] < data['Open'][i-1] and data['Open'][i] < data['Close'][i] and (data['Close'][i] - data['Open'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6 and data['Close'][i-2] < data['Close'][i-1] and data['Open'][i] < data['Close'][i-2]:
        bullish_morning_star = True
        output += f"Bullish Morning Star pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Doji Pattern
bullish_doji = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]) and data['Close'][i] > data['Open'][i]:
        bullish_doji = True
        output += f"Bullish Doji pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Identify Bull Flag pattern
bull_flag = False
for i in range(1, len(data)-1):
    if data['Low'][i] > data['Low'][i-1] and data['High'][i] < data['High'][i+1] and data['Close'][i] > data['Open'][i] and data['Open'][i+1] > data['Close'][i] and data['Close'][i+1] > data['Open'][i]:
        bull_flag = True
        output += f"Bull Flag pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Deliberation pattern
bullish_deliberation = False
for i in range(2, len(data)-2):
    if data['Open'][i] < data['Open'][i-1] and data['Open'][i] > data['Open'][i+1] and data['Open'][i] < data['Close'][i-1] and data['Open'][i] > data['Close'][i-2]:
        bullish_deliberation = True
        output += f"Bullish Deliberation pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Closing Marubozu pattern
bullish_closing_marubozu = False
for i in range(1, len(data)-1):
    if data['Open'][i] > data['Close'][i] and data['Close'][i] > data['High'][i] and data['Open'][i] == data['Low'][i] and data['Close'][i] == data['High'][i]:
        bullish_closing_marubozu = True
        output += f"Bullish Closing Marubozu pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Stalled Pattern
bullish_stalled = False
for i in range(1, len(data)-1):
    if data['Open'][i] == data['Close'][i] and data['Open'][i-1] > data['Close'][i-1] and data['Open'][i] > data['Open'][i-1]:
        bullish_stalled = True
        output += f"Bullish Stalled Pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Kicking pattern
bullish_kicking = False
for i in range(1, len(data)-1):
    if data['Open'][i] < data['Close'][i] and data['Open'][i-1] > data['Close'][i-1] and data['Open'][i] > data['Open'][i-1] and data['Close'][i] > data['Open'][i]:
        bullish_kicking = True
        output += f"Bullish Kicking pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_homing_pigeon = False
for i in range(1, len(data)-1):
    if data['Open'][i] < data['Close'][i] and data['Open'][i-1] > data['Close'][i-1] and data['Open'][i] > data['Open'][i-1] and data['Close'][i] > data['Open'][i]:
        bullish_homing_pigeon = True
        output += f"Bullish Homing Pigeon pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Belt Hold pattern
bullish_belt_hold = False
for i in range(1, len(data)-1):
    if data['Open'][i] < data['Close'][i] and data['Open'][i] == data['Low'][i] and data['Open'][i] == data['High'][i] and data['Open'][i] == data['Close'][i-1] and data['Close'][i] > data['Open'][i-1]:
        bullish_belt_hold = True
        output += f"Bullish Belt Hold pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Thrust pattern
bullish_thrust = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Open'][i] and data['Close'][i-1] > data['Open'][i-1] and data['Close'][i] > data['Open'][i-1]:
        bullish_thrust = True
        output += f"Bullish Thrust pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Separating Lines pattern
bullish_separating_lines = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Open'][i] and data['Open'][i-1] < data['Close'][i-1] and data['Close'][i] > data['Open'][i-1]:
        bullish_separating_lines = True
        output += f"Bullish Separating Lines pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Meeting Lines pattern
bullish_meeting_lines = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Open'][i] and data['High'][i] <= data['High'][i-1] and data['Low'][i] >= data['Low'][i-1]:
        bullish_meeting_lines = True
        output += f"Bullish Meeting Lines pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Kicker pattern
bullish_kicker = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Open'][i] and data['Close'][i-1] > data['Open'][i-1] and data['Open'][i] > data['Close'][i-1]:
        bullish_kicker = True
        output += f"Bullish Kicker pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Inverted Hammer pattern
bullish_inverted_hammer = False
for i in range(1, len(data)-1):
    if (data['Low'][i] < data['Open'][i] and data['Low'][i] < data['Close'][i]
    and abs(data['Open'][i] - data['Close'][i]) <= 0.1 * (data['High'][i-1] - data['Low'][i-1])
    and data['Open'][i-1] > data['Close'][i-1]):
        bullish_inverted_hammer = True
        output += f"Bullish Inverted Hammer pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Upside Gap Three Methods pattern
bullish_upside_gap_three_methods = False
for i in range(3, len(data)-3):
    if (data['Open'][i] < data['Close'][i]
    and data['Close'][i] > data['Open'][i-1] and data['Open'][i-1] > data['Close'][i-1]
    and data['Close'][i-1] > data['Open'][i-2] and data['Open'][i-2] > data['Close'][i-2]
    and data['Close'][i-2] > data['Open'][i-3] and data['Open'][i-3] > data['Close'][i-3]
    and data['Open'][i-1] < data['Close'][i-3] and data['Open'][i] < data['Close'][i-3]):
        bullish_upside_gap_three_methods = True
        output += f"Bullish Upside Gap Three Methods pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bullish Three River Bottom pattern
bullish_three_river_bottom = False
for i in range(5, len(data)-5):
    if (data['Low'][i] < data['Low'][i-1] and data['Low'][i-1] < data['Low'][i-2]
    and data['Low'][i-2] > data['Low'][i-3] and data['Low'][i-3] < data['Low'][i-4]
    and data['Low'][i-4] < data['Low'][i-5] and data['High'][i] > data['High'][i-1]
    and data['High'][i-1] > data['High'][i-2] and data['High'][i-2] < data['High'][i-3]
    and data['High'][i-3] > data['High'][i-4] and data['High'][i-4] > data['High'][i-5]):
        bullish_three_river_bottom = True
        output += f"Bullish Three River Bottom pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_ladder_bottom = False

for i in range(3, len(data)):
    # Check for descending candlesticks
    is_descending = all(data['Close'][i-j] < data['Close'][i-j-1] for j in range(3))
    # Check for small real bodies and small or nonexistent shadows
    is_small_candles = all((data['Open'][i-j] > data['Close'][i-j]) and
                           (abs(data['Open'][i-j] - data['Close'][i-j]) < (0.1 * (data['High'][i-j] - data['Low'][i-j]))) for j in range(3))
    # Check for larger bullish engulfing candlestick
    is_bullish_engulfing = (data['Open'][i] < data['Close'][i-3]) and \
                           (data['Close'][i] > data['Open'][i-3]) and \
                           (data['Open'][i] < data['Close'][i-2]) and \
                           (data['Close'][i] > data['Open'][i-2]) and \
                           (data['Open'][i] < data['Close'][i-1]) and \
                           (data['Close'][i] > data['Open'][i-1]) and \
                           (data['Open'][i] < data['Close'][i-4]) and \
                           (data['Close'][i] > data['Open'][i-4])

    if is_descending and is_small_candles and is_bullish_engulfing:
        bullish_ladder_bottom = True
        output += f"Bullish Ladder Bottom pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_thrusting = False

for i in range(1, len(data)):
    # Check for a large bearish candlestick
    is_large_bearish = (data['Open'][i-1] > data['Close'][i-1]) and \
                       ((data['Open'][i-1] - data['Close'][i-1]) > (0.5 * (data['High'][i-1] - data['Low'][i-1])))
    # Check for a smaller bullish candlestick
    is_smaller_bullish = (data['Close'][i] > data['Open'][i-1]) and \
                         (data['Close'][i] > ((data['Open'][i-1] + data['Close'][i-1]) / 2))
    
    if is_large_bearish and is_smaller_bullish:
        bullish_thrusting = True
        output += f"Bullish Thrusting pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_deliberation = False

for i in range(2, len(data)):
    # Check for the first two bearish candlesticks with small real bodies and overlap
    is_bearish_1 = (data['Close'][i-2] < data['Open'][i-2]) and ((data['Open'][i-2] - data['Close'][i-2]) / (data['High'][i-2] - data['Low'][i-2]) < 0.2)
    is_bearish_2 = (data['Close'][i-1] < data['Open'][i-1]) and ((data['Open'][i-1] - data['Close'][i-1]) / (data['High'][i-1] - data['Low'][i-1]) < 0.2)
    are_bearish_overlap = (data['High'][i-2] > data['High'][i-1]) and (data['Low'][i-2] < data['Low'][i-1])
    
    # Check for the third bullish candlestick that engulfs the previous two bearish candlesticks
    is_bullish_3 = (data['Open'][i] < data['Close'][i]) and (data['Open'][i] > data['Close'][i-2]) and (data['Close'][i] < data['Open'][i-1]) and (data['Close'][i] < data['Open'][i-2])
    
    if is_bearish_1 and is_bearish_2 and are_bearish_overlap and is_bullish_3:
        bullish_deliberation = True
        output += f"Bullish Deliberation pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_rising_three_methods = False

for i in range(4, len(data)):
    # Check for the first bearish candlestick
    is_bearish_1 = data['Close'][i-4] < data['Open'][i-4]
    
    # Check for the three small bullish candlesticks contained within the range of the first bearish candlestick
    are_bullish_2_4 = all(data['Open'][i-j] < data['High'][i-4] and data['Close'][i-j] > data['Low'][i-4] for j in range(3, 0, -1))
    
    # Check for the fifth bullish candlestick that closes above the range of the first bearish candlestick
    is_bullish_5 = data['Close'][i] > data['High'][i-4]
    
    if is_bearish_1 and are_bullish_2_4 and is_bullish_5:
        bullish_rising_three_methods = True
        output += f"Bullish Rising Three Methods pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_three_method_formation = False

for i in range(4, len(data)):
    # Check for the first bearish candlestick
    is_bearish_1 = data['Close'][i-4] < data['Open'][i-4]
    
    # Check for the three small bullish candlesticks contained within the range of the first bearish candlestick
    are_bullish_2_4 = all(data['Open'][i-j] < data['High'][i-4] and data['Close'][i-j] > data['Low'][i-4] for j in range(3, 0, -1))
    
    # Check for the fifth bullish candlestick that closes above the range of the first bearish candlestick
    is_bullish_5 = data['Close'][i] > data['High'][i-4]
    
    if is_bearish_1 and are_bullish_2_4 and is_bullish_5:
        bullish_three_method_formation = True
        output += f"Bullish Three-Method Formation pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_three_line_strike = False

for i in range(3, len(data)):
    # Check for the first three bearish candlesticks
    are_bearish_1_3 = all(data['Close'][i-j] < data['Open'][i-j] for j in range(3, 0, -1))
    
    # Check for the fourth bullish candlestick that gaps up above the high of the third bearish candlestick
    is_bullish_4 = data['Open'][i] > data['High'][i-3] and data['Close'][i] > data['Open'][i-3]
    
    if are_bearish_1_3 and is_bullish_4:
        bullish_three_line_strike = True
        output += f"Bullish Three-Line Strike pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_concealing_baby_swallow = False

for i in range(4, len(data)):
    # Check for the first four bearish candlesticks
    are_bearish_1_4 = all(data['Close'][i-j] < data['Open'][i-j] for j in range(4, 0, -1))
    
    # Check for a doji or small bearish candlestick as the third candlestick
    is_doji_or_small_bearish = data['Open'][i-2] > data['Close'][i-2] and (data['Open'][i-2] - data['Close'][i-2]) / (data['High'][i-2] - data['Low'][i-2]) < 0.1
    
    # Check for a bullish candlestick that engulfs the previous bearish candlesticks as the fifth candlestick
    is_bullish_5 = data['Open'][i] < data['Close'][i-1] and data['Close'][i] > data['Open'][i-1] and data['Close'][i] > data['Open'][i-2] and data['Open'][i] < data['Close'][i-3]
    
    if are_bearish_1_4 and is_doji_or_small_bearish and is_bullish_5:
        bullish_concealing_baby_swallow = True
        output += f"Bullish Concealing Baby Swallow pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_opening_marubozu = False

for i in range(1, len(data)):
    # Check for a long bullish candlestick with no or very small shadows
    is_bullish_marubozu = data['Close'][i] > data['Open'][i] and (data['Close'][i] - data['Low'][i]) / (data['High'][i] - data['Low'][i]) > 0.9
    
    if is_bullish_marubozu:
        bullish_opening_marubozu = True
        output += f"Bullish Opening Marubozu pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_modified_hikkake = False

for i in range(3, len(data)):
    # Check for lower lows and lower highs
    is_lower_lows = data['Low'][i] < data['Low'][i-1] and data['High'][i] < data['High'][i-1]
    is_lower_highs = data['High'][i] < data['High'][i-2]
    
    # Check for a smaller inside candlestick followed by a bullish candlestick breaking above the inside candlestick's high
    is_inside_candlestick = data['Low'][i-1] > data['Low'][i] and data['High'][i-1] > data['High'][i]
    is_bullish_breakout = data['Close'][i] > data['High'][i-1]
    
    if is_lower_lows and is_lower_highs and is_inside_candlestick and is_bullish_breakout:
        bullish_modified_hikkake = True
        output += f"Bullish Modified Hikkake pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_hikkake = False

for i in range(3, len(data)):
    # Check for lower highs and lower lows
    is_lower_highs = data['High'][i] < data['High'][i-1] and data['Low'][i] < data['Low'][i-1]
    is_lower_lows = data['Low'][i] < data['Low'][i-2]
    
    # Check for a smaller inside candlestick followed by a bullish candlestick breaking above the inside candlestick's high
    is_inside_candlestick = data['High'][i-1] > data['High'][i] and data['Low'][i-1] > data['Low'][i]
    is_bullish_breakout = data['Close'][i] > data['High'][i-1]
    
    if is_lower_highs and is_lower_lows and is_inside_candlestick and is_bullish_breakout:
        bullish_hikkake = True
        output += f"Bullish Hikkake pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_high_wave_candle = False

for i in range(len(data)):
    body_height = abs(data['Close'][i] - data['Open'][i])
    upper_wick = data['High'][i] - max(data['Close'][i], data['Open'][i])
    lower_wick = min(data['Close'][i], data['Open'][i]) - data['Low'][i]
    
    # Check for a small body and long upper and lower wicks
    if body_height < upper_wick and body_height < lower_wick:
        bullish_high_wave_candle = True
        output += f"Bullish High Wave Candle pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_three_inside_up = False

for i in range(2, len(data)):
    # Check for the bullish three inside up pattern
    if data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Close'][i-1] < data['Close'][i-2] and \
       data['Open'][i] < data['Close'][i-1] and \
       data['Close'][i] > data['Open'][i-1]:
        bullish_three_inside_up = True
        output += f"Bullish Three Inside Up pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_three_outside_up = False

for i in range(2, len(data)):
    # Check for the bullish three outside up pattern
    if data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Close'][i-1] < data['Close'][i-2] and \
       data['Open'][i] < data['Close'][i-1] and \
       data['Close'][i] > data['Open'][i-1]:
        bullish_three_outside_up = True
        output += f"Bullish Three Outside Up pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_three_white_soldiers = False

for i in range(2, len(data)):
    # Check for the bullish three white soldiers pattern
    if data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i] > data['Open'][i] and \
       data['Close'][i] > data['Close'][i-1] and \
       data['Close'][i-1] > data['Close'][i-2]:
        bullish_three_white_soldiers = True
        output += f"Bullish Three White Soldiers pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_dragonfly_doji = False

for i in range(len(data)):
    # Check for the bullish dragonfly doji pattern
    if data['Open'][i] == data['Low'][i] and \
       data['Open'][i] == data['Close'][i] and \
       data['High'][i] > data['Open'][i]:
        bullish_dragonfly_doji = True
        output += f"Bullish Dragonfly Doji pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_spinning_top = False

for i in range(len(data)):
    # Check for the bullish spinning top pattern
    if data['Open'][i] == data['Close'][i] and \
       (data['High'][i] - data['Open'][i]) > 2 * (data['Close'][i] - data['Low'][i]) and \
       (data['Close'][i] - data['Low'][i]) <= 0.25 * (data['High'][i] - data['Low'][i]) and \
       (data['Close'][i] > data['Open'][i]):
        bullish_spinning_top = True
        output += f"Bullish Spinning Top pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_advance_block = False

for i in range(2, len(data)):
    # Check for the bullish advance block pattern
    if data['High'][i-2] < data['High'][i-1] < data['High'][i] and \
       data['Low'][i-2] > data['Low'][i-1] > data['Low'][i] and \
       (data['Open'][i] < data['Open'][i-1] or data['Close'][i] < data['Close'][i-1]):
        bullish_advance_block = True
        output += f"Bullish Advance Block pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_side_by_side_white_lines = False

for i in range(2, len(data)):
    # Check for the Bullish Side-by-Side White Lines pattern
    if abs(data['Open'][i] - data['Close'][i]) <= 0.0001 and \
       abs(data['Open'][i-1] - data['Close'][i-1]) <= 0.0001 and \
       data['Close'][i] > data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Open'][i] < data['Close'][i-1]:
        bullish_side_by_side_white_lines = True
        output += f"Bullish Side-by-Side White Lines pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_breakaway = False

for i in range(4, len(data)):
    # Check for the Bullish Breakaway pattern
    if data['Close'][i] < data['Open'][i] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Close'][i-2] < data['Open'][i-2] and \
       data['Close'][i-3] < data['Open'][i-3] and \
       data['Close'][i-4] < data['Open'][i-4] and \
       data['Open'][i] < data['Close'][i-1] and \
       data['Close'][i] > data['Open'][i-1] and \
       data['Close'][i] > data['Close'][i-1]:
        bullish_breakaway = True
        output += f"Bullish Breakaway pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

upside_tasuki_gap = False

for i in range(3, len(data)):
    # Check for the Upside Tasuki Gap pattern
    if data['Open'][i] < data['Close'][i] and \
       data['Open'][i-1] < data['Close'][i-1] and \
       data['Close'][i-1] < data['Open'][i] and \
       data['Open'][i-2] < data['Close'][i-2] and \
       data['Close'][i-2] < data['Open'][i-1]:
        upside_tasuki_gap = True
        output += f"Upside Tasuki Gap pattern identified at date: {data['Date'][i]}\n"
        break
for i in range(1, len(data)):
    # Check for the Tweezer Top pattern
    if data['High'][i] == data['High'][i-1] and \
       data['Low'][i] == data['Low'][i-1] and \
       data['Close'][i] < data['Open'][i] and \
       data['Open'][i-1] < data['Close'][i-1]:
        tweezer_top = True
        output += f"Tweezer Top pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

piercing_pattern = False

for i in range(1, len(data)):
    # Check for the Piercing Pattern
    if data['Close'][i] < data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i] > data['Low'][i-1] + (data['High'][i-1] - data['Low'][i-1]) / 2 and \
       data['Close'][i] < data['Open'][i-1]:
        piercing_pattern = True
        output += f"Piercing Pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

rectangle_pattern = False

for i in range(1, len(data)):
    # Check for the Rectangles (Continuation Pattern)
    if data['High'][i] <= data['High'][i-1] and \
       data['Low'][i] >= data['Low'][i-1] and \
       data['High'][i] >= data['Low'][i-1] and \
       data['Low'][i] <= data['High'][i-1]:
        rectangle_pattern = True
        output += f"Rectangles (Continuation Pattern) identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

diamond_bottom_pattern = False

for i in range(3, len(data)):
    # Check for the Diamond Bottom pattern
    if data['High'][i] <= data['High'][i-1] and \
       data['High'][i] <= data['High'][i-2] and \
       data['Low'][i] >= data['Low'][i-1] and \
       data['Low'][i] >= data['Low'][i-2] and \
       data['High'][i-1] <= data['High'][i-2] and \
       data['Low'][i-1] <= data['Low'][i-2]:
        diamond_bottom_pattern = True
        output += f"Diamond Bottom pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

inverse_head_and_shoulders = False

for i in range(2, len(data)-2):
    # Check for the Inverse Head and Shoulders pattern
    if data['Low'][i] < data['Low'][i-1] and \
       data['Low'][i] < data['Low'][i+1] and \
       data['Low'][i-1] < data['Low'][i-2] and \
       data['Low'][i+1] < data['Low'][i+2] and \
       data['Low'][i-1] < data['Low'][i+1] and \
       data['High'][i] > data['High'][i-1] and \
       data['High'][i] > data['High'][i+1] and \
       data['High'][i-1] > data['High'][i-2] and \
       data['High'][i+1] > data['High'][i+2] and \
       data['High'][i-1] > data['High'][i+1]:
        inverse_head_and_shoulders = True
        output += f"Inverse Head and Shoulders pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

ascending_triangle = False

for i in range(2, len(data)):
    # Check for the Ascending Triangle pattern
    if data['High'][i] == data['High'][i-1] and \
       data['High'][i-1] == data['High'][i-2] and \
       data['Low'][i] > data['Low'][i-1] and \
       data['Low'][i] > data['Low'][i-2]:
        ascending_triangle = True
        output += f"Ascending Triangle pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_pennant = False

for i in range(1, len(data)):
    # Check for the Bullish Pennant pattern
    if data['Low'][i] < data['Low'][i-1] and \
       data['High'][i] > data['High'][i-1]:
        bullish_pennant = True
        output += f"Bullish Pennant pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

falling_wedge = False

for i in range(2, len(data)):
    # Check for the Falling Wedge pattern
    if data['High'][i] < data['High'][i-1] and \
       data['Low'][i] < data['Low'][i-1] and \
       data['High'][i-1] < data['High'][i-2] and \
       data['Low'][i-1] < data['Low'][i-2]:
        falling_wedge = True
        output += f"Falling Wedge pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_counterattack = False

for i in range(1, len(data)):
    # Check for the Bullish Counterattack pattern
    if data['Open'][i] < data['Close'][i] and \
       data['Open'][i-1] > data['Close'][i-1] and \
       data['Open'][i] < data['Open'][i-1] and \
       data['Close'][i] > data['Close'][i-1]:
        bullish_counterattack = True
        output  += f"Bullish Counterattack pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_abandoned_baby = False

for i in range(2, len(data)):
    # Check for the Bullish Abandoned Baby pattern
    if data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Open'][i] < data['Close'][i-1] and \
       data['Close'][i] > data['Open'][i] and \
       data['Low'][i] > data['Low'][i-2] and \
       data['High'][i] > data['High'][i-1]:
        bullish_abandoned_baby = True
        output += f"Bullish Abandoned Baby pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

for i in range(1, len(data)):
    # Check for the Bullish Rickshaw Man pattern
    if data['Open'][i] == data['Close'][i] and \
       (data['Open'][i] - data['Low'][i] >= 2 * (data['High'][i] - data['Open'][i])):
        bullish_rickshaw_man = True
        output += f"Bullish Rickshaw Man pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_continuation_diamond = False

for i in range(3, len(data)-2):
    # Check for the Bullish Continuation Diamond pattern
    if data['High'][i] > data['High'][i-1] and \
       data['High'][i] > data['High'][i-2] and \
       data['High'][i-1] < data['High'][i-2] and \
       data['Low'][i] < data['Low'][i-1] and \
       data['Low'][i] < data['Low'][i-2] and \
       data['Low'][i-1] > data['Low'][i-2] and \
       data['Close'][i] > data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i-1] < data['Open'][i] and \
       data['Open'][i-1] > data['Close'][i] and \
       data['Open'][i-1] < data['Open'][i]:
        bullish_continuation_diamond = True
        output += f"Bullish Continuation Diamond pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_price_channel = False

for i in range(2, len(data)):
    # Check for the bullish price channel pattern
    if data['High'][i] > data['High'][i-1] and \
       data['Low'][i] > data['Low'][i-1] and \
       data['High'][i-1] < data['High'][i-2] and \
       data['Low'][i-1] < data['Low'][i-2]:
        bullish_price_channel = True
        output += f"Bullish Price Channel pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print(output)
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_on_neckline = False

for i in range(2, len(data)):
    # Check for the Bullish On Neckline pattern
    if data['Close'][i] > data['Open'][i] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Close'][i] <= data['Low'][i-1] and \
       data['Close'][i] >= data['Low'][i]:
        bullish_on_neckline = True
        output += f"Bullish On Neckline pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_in_neckline = False

for i in range(2, len(data)):
    # Check for the Bearish In Neckline pattern
    if data['Close'][i] < data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i] >= data['High'][i-1] and \
       data['Close'][i] <= data['High'][i]:
        bearish_in_neckline = True
        output += f"Bearish In Neckline pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

for i in range(2, len(data)):
    # Check for Bullish Three White Soldiers pattern
    if data['Close'][i] > data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i-2] > data['Open'][i-2] and \
       data['Open'][i] < data['Close'][i-1] and \
       data['Open'][i] < data['Close'][i-2] and \
       data['Close'][i] > data['Open'][i-1] and \
       data['Close'][i] > data['Open'][i-2] and \
       data['High'][i] > data['High'][i-1] and \
       data['High'][i-1] > data['High'][i-2]:
        bullish_three_white_soldiers = True

    # Check for Rectangles pattern
    if data['Close'][i] == data['Close'][i-1] and \
       data['Low'][i] > data['Low'][i-1] and \
       data['High'][i] < data['High'][i-1]:
        rectangles = True
        
# Check if both patterns were identified
if bullish_three_white_soldiers and rectangles:
    output += "Bullish Three White Soldiers + Rectangles combination pattern identified."
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

for i in range(2, len(data)):
    if data['Low'][i] > data['Low'][i-1] and \
       data['Low'][i-1] > data['Low'][i-2]:
        bullish_inverted_triangle = True
        output += f"Higher lows found at dates: {data['Date'][i-2]}, {data['Date'][i-1]}, {data['Date'][i]}\n"
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Look for a horizontal or slightly ascending resistance level
if bullish_inverted_triangle:
    resistance_level = data['High'].nunique() <= 2
    if resistance_level:
        output += "Bullish Inverted Triangle pattern identified."
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_megaphone = False

# Look for expanding trendlines
for i in range(4, len(data)):
    if data['High'][i] > data['High'][i-1] and \
       data['Low'][i] < data['Low'][i-1] and \
       data['High'][i] < data['High'][i-2] and \
       data['Low'][i] > data['Low'][i-2] and \
       data['High'][i] > data['High'][i-3] and \
       data['Low'][i] < data['Low'][i-3] and \
       data['High'][i] < data['High'][i-4] and \
       data['Low'][i] > data['Low'][i-4]:
        bullish_megaphone = True
        output += f"Bullish Megaphone pattern identified at date: {data['Date'][i]}\n"
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bullish_gartley = False

# Look for Bullish Gartley pattern
for i in range(4, len(data)):
    if data['High'][i] > data['High'][i-1] and \
       data['High'][i] > data['High'][i-2] and \
       data['High'][i-1] < data['Low'][i-2] and \
       data['High'][i-3] > data['High'][i-1] and \
       data['Low'][i] < data['Low'][i-1] and \
       data['Close'][i] > data['Open'][i] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       (data['Open'][i] - data['Low'][i]) / (data['High'][i] - data['Low'][i]) >= 0.618 and \
       (data['High'][i] - data['Low'][i-1]) / (data['High'][i] - data['Low'][i]) >= 0.618:
        bullish_gartley = True
        output += f"Bullish Gartley pattern identified at date: {data['Date'][i]}\n"
        break
    

bullish_butterfly = False

# Look for Bullish Butterfly pattern
for i in range(5, len(data)):
    if data['Low'][i] < data['Low'][i-1] and \
       data['Low'][i] < data['Low'][i-2] and \
       data['High'][i] > data['Low'][i-2] and \
       data['Low'][i-3] < data['Low'][i-1] and \
       data['High'][i] < data['High'][i-1] and \
       data['High'][i-3] > data['Low'][i-2] and \
       data['Low'][i-3] < data['Low'][i-1] and \
       data['High'][i-4] < data['Low'][i-1] and \
       data['High'][i-4] > data['Low'][i-3]:
        bullish_butterfly = True
        output += f"Bullish Butterfly pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    symbol = 'PLTR'
    qty = 100

    # define the thresholds for selling the stock
    sell_up_threshold = 0.003  # 0.3%
    sell_down_threshold = -0.0015  # -0.15%

    # buy one share of the stock
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

####### Bearish patherns sterated here######################################################################
bearish_butterfly = False

# Look for Bearish Butterfly pattern
for i in range(5, len(data)):
    if data['High'][i] > data['High'][i-1] and \
       data['High'][i] > data['High'][i-2] and \
       data['Low'][i] < data['High'][i-2] and \
       data['High'][i-3] > data['High'][i-1] and \
       data['Low'][i] > data['Low'][i-1] and \
       data['Low'][i-3] < data['High'][i-2] and \
       data['High'][i-3] > data['High'][i-1] and \
       data['Low'][i-4] > data['High'][i-1] and \
       data['Low'][i-4] < data['High'][i-3]:
        bearish_butterfly = True
        output += f"Bearish Butterfly pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_gartley = False

# Look for Bearish Gartley pattern
for i in range(4, len(data)):
    if data['Low'][i] < data['Low'][i-1] and \
       data['Low'][i] < data['Low'][i-2] and \
       data['High'][i-1] > data['Low'][i-2] and \
       data['Low'][i-3] < data['Low'][i-1] and \
       data['High'][i] > data['High'][i-1] and \
       data['Close'][i] < data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       (data['High'][i] - data['Low'][i]) / (data['High'][i] - data['Low'][i-1]) >= 0.618 and \
       (data['High'][i] - data['Low'][i]) / (data['High'][i] - data['Low'][i-2]) >= 0.618:
        bearish_gartley = True
        output += f"Bearish Gartley pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_megaphone = False

for i in range(4, len(data)):
    if data['High'][i] < data['High'][i-1] and \
       data['Low'][i] > data['Low'][i-1] and \
       data['High'][i] > data['High'][i-2] and \
       data['Low'][i] < data['Low'][i-2] and \
       data['High'][i] < data['High'][i-3] and \
       data['Low'][i] > data['Low'][i-3] and \
       data['High'][i] > data['High'][i-4] and \
       data['Low'][i] < data['Low'][i-4]:
        bearish_megaphone = True
        output += f"Bearish Megaphone pattern identified at date: {data['Date'][i]}\n"
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_price_channel = False

for i in range(2, len(data)):
    # Check for the bearish price channel pattern
    if data['High'][i] < data['High'][i-1] and \
       data['Low'][i] < data['Low'][i-1] and \
       data['High'][i-1] > data['High'][i-2] and \
       data['Low'][i-1] > data['Low'][i-2]:
        bearish_price_channel = True
        output += f"Bearish Price Channel pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_rickshaw_man = False

for i in range(1, len(data)):
    # Check for the Bearish Rickshaw Man pattern
    if data['Open'][i] == data['Close'][i] and \
       (data['High'][i] - data['Open'][i] >= 2 * (data['Open'][i] - data['Low'][i])):
        bearish_rickshaw_man = True
        output += f"Bearish Rickshaw Man pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_abandoned_baby = False

for i in range(2, len(data)):
    # Check for the Bearish Abandoned Baby pattern
    if data['Close'][i-2] < data['Open'][i-2] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Open'][i] > data['Close'][i-1] and \
       data['Close'][i] < data['Open'][i] and \
       data['Low'][i] < data['Low'][i-2] and \
       data['High'][i] < data['Low'][i-1]:
        bearish_abandoned_baby = True
        output += f"Bearish Abandoned Baby pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_counterattack = False

for i in range(1, len(data)):
    # Check for the Bearish Counterattack pattern
    if data['Open'][i] > data['Close'][i] and \
       data['Open'][i-1] < data['Close'][i-1] and \
       data['Open'][i] > data['Open'][i-1] and \
       data['Close'][i] < data['Close'][i-1]:
        bearish_counterattack = True
        output += f"Bearish Counterattack pattern identified at date: {data['Date'][i]}\n"
        break
rising_wedge = False

for i in range(2, len(data)):
    # Check for the Rising Wedge pattern
    if data['High'][i] > data['High'][i-1] and \
       data['Low'][i] > data['Low'][i-1] and \
       data['High'][i-1] > data['High'][i-2] and \
       data['Low'][i-1] > data['Low'][i-2]:
        rising_wedge = True
        output += f"Rising Wedge pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_pennant = False

for i in range(1, len(data)):
    # Check for the Bearish Pennant pattern
    if data['High'][i] > data['High'][i-1] and \
       data['Low'][i] < data['Low'][i-1]:
        bearish_pennant = True
        output += f"Bearish Pennant pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

diamond_top_pattern = False

for i in range(3, len(data)):
    # Check for the Diamond Top pattern
    if data['Low'][i] >= data['Low'][i-1] and \
       data['Low'][i] >= data['Low'][i-2] and \
       data['High'][i] <= data['High'][i-1] and \
       data['High'][i] <= data['High'][i-2] and \
       data['Low'][i-1] >= data['Low'][i-2] and \
       data['High'][i-1] >= data['High'][i-2]:
        diamond_top_pattern = True
        output += f"Diamond Top pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

tweezer_bottom = False

for i in range(1, len(data)):
    # Check for the Tweezer Bottom pattern
    if data['Low'][i] == data['Low'][i-1] and \
       data['High'][i] == data['High'][i-1] and \
       data['Close'][i] > data['Open'][i] and \
       data['Open'][i-1] > data['Close'][i-1]:
        tweezer_bottom = True
        output += f"Tweezer Bottom pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_belt_hold = False

for i in range(1, len(data)):
    # Check for the Bearish Belt Hold pattern
    if data['Open'][i] > data['Close'][i] and \
       data['Open'][i-1] > data['Close'][i-1] and \
       data['Open'][i] == data['High'][i] and \
       data['Close'][i] == data['Low'][i]:
        bearish_belt_hold = True
        output += f"Bearish Belt Hold pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

downside_tasuki_gap = False

for i in range(3, len(data)):
    # Check for the Downside Tasuki Gap pattern
    if data['Open'][i] > data['Close'][i] and \
       data['Open'][i-1] > data['Close'][i-1] and \
       data['Close'][i-1] > data['Open'][i] and \
       data['Open'][i-2] > data['Close'][i-2] and \
       data['Close'][i-2] > data['Open'][i-1]:
        downside_tasuki_gap = True
        output += f"Downside Tasuki Gap pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_breakaway = False

for i in range(4, len(data)):
    # Check for the Bearish Breakaway pattern
    if data['Close'][i] > data['Open'][i] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i-3] > data['Open'][i-3] and \
       data['Close'][i-4] > data['Open'][i-4] and \
       data['Open'][i] > data['Close'][i-1] and \
       data['Close'][i] < data['Open'][i-1] and \
       data['Close'][i] < data['Close'][i-1]:
        bearish_breakaway = True
        output += f"Bearish Breakaway pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_island_reversal = False

for i in range(2, len(data)):
    # Check for the Bearish Island Reversal pattern
    if data['Open'][i] > data['Close'][i-1] and \
       data['Close'][i] > data['Open'][i-1] and \
       data['Low'][i] > data['High'][i-1] and \
       data['High'][i] < data['Low'][i-1]:
        bearish_island_reversal = True
        output += f"Bearish Island Reversal pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()


bearish_stick_sandwich = False

for i in range(2, len(data)):
    # Check for the Bearish Stick Sandwich pattern
    if data['Close'][i] > data['Open'][i] and \
       data['Open'][i-1] > data['Close'][i-1] and \
       data['Close'][i-2] > data['Open'][i-2] and \
       data['Close'][i] < data['Close'][i-2] and \
       data['Open'][i] > data['Close'][i-1] and \
       data['Close'][i] < data['Open'][i-1]:
        bearish_stick_sandwich = True
        output += f"Bearish Stick Sandwich pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_side_by_side_white_lines = False

for i in range(2, len(data)):
    # Check for the Bearish Side-by-Side White Lines pattern
    if abs(data['Open'][i] - data['Close'][i]) <= 0.0001 and \
       abs(data['Open'][i-1] - data['Close'][i-1]) <= 0.0001 and \
       data['Close'][i] < data['Open'][i] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Open'][i] > data['Close'][i-1]:
        bearish_side_by_side_white_lines = True
        output += f"Bearish Side-by-Side White Lines pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()


bearish_advance_block = False

for i in range(2, len(data)):
    # Check for the bearish advance block pattern
    if data['High'][i-2] > data['High'][i-1] > data['High'][i] and \
       data['Low'][i-2] < data['Low'][i-1] < data['Low'][i] and \
       (data['Open'][i] > data['Open'][i-1] or data['Close'][i] > data['Close'][i-1]):
        bearish_advance_block = True
        output += f"Bearish Advance Block pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_descending_hawk = False

for i in range(2, len(data)):
    # Check for the bearish descending hawk pattern
    if data['High'][i-2] > data['High'][i-1] > data['High'][i] and \
       data['Low'][i-2] > data['Low'][i-1] > data['Low'][i]:
        bearish_descending_hawk = True
        output += f"Bearish Descending Hawk pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_spinning_top = False

for i in range(len(data)):
    # Check for the bearish spinning top pattern
    if data['Open'][i] == data['Close'][i] and \
       (data['High'][i] - data['Open'][i]) > 2 * (data['Close'][i] - data['Low'][i]) and \
       (data['Close'][i] - data['Low'][i]) <= 0.25 * (data['High'][i] - data['Low'][i]) and \
       (data['Close'][i] < data['Open'][i]):
        bearish_spinning_top = True
        output += f"Bearish Spinning Top pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_hanging_man = False

for i in range(len(data)):
    # Check for the bearish hanging man pattern
    if data['Open'][i] == data['High'][i] and \
       data['Close'][i] < data['Open'][i] and \
       (data['Open'][i] - data['Low'][i]) >= 2 * (data['Close'][i] - data['Open'][i]) and \
       (data['Close'][i] - data['Low'][i]) <= 0.1 * (data['Open'][i] - data['Low'][i]):
        bearish_hanging_man = True
        output += f"Bearish Hanging Man pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_gravestone_doji = False

for i in range(len(data)):
    # Check for the bearish gravestone doji pattern
    if data['Open'][i] == data['High'][i] and \
       data['Open'][i] == data['Close'][i] and \
       data['Low'][i] < data['Open'][i]:
        bearish_gravestone_doji = True
    output += f"Bearish Gravestone Doji pattern identified at date: {data['Date'][i]}\n"
    break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_three_black_crows = False

for i in range(2, len(data)):
    # Check for the bearish three black crows pattern
    if data['Close'][i-2] < data['Open'][i-2] and \
       data['Close'][i-1] < data['Open'][i-1] and \
       data['Close'][i] < data['Open'][i] and \
       data['Close'][i] < data['Close'][i-1] and \
       data['Close'][i-1] < data['Close'][i-2]:
        bearish_three_black_crows = True
        output += f"Bearish Three Black Crows pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_three_outside_down = False

for i in range(2, len(data)):
    # Check for the bearish three outside down pattern
    if data['Close'][i-2] < data['Open'][i-2] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i-1] > data['Close'][i-2] and \
       data['Open'][i] > data['Close'][i-1] and \
       data['Close'][i] < data['Open'][i-1]:
        bearish_three_outside_down = True
        output += f"Bearish Three Outside Down pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_three_inside_down = False

for i in range(2, len(data)):
    # Check for the bearish three inside down pattern
    if data['Close'][i-2] < data['Open'][i-2] and \
       data['Close'][i-1] > data['Open'][i-1] and \
       data['Close'][i-1] > data['Close'][i-2] and \
       data['Open'][i] > data['Close'][i-1] and \
       data['Close'][i] < data['Open'][i-1]:
        bearish_three_inside_down = True
        output += f"Bearish Three Inside Down pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_high_wave_candle = False

for i in range(len(data)):
    body_height = abs(data['Close'][i] - data['Open'][i])
    upper_wick = data['High'][i] - max(data['Close'][i], data['Open'][i])
    lower_wick = min(data['Close'][i], data['Open'][i]) - data['Low'][i]
    
    # Check for a small body and long upper and lower wicks
    if body_height < upper_wick and body_height < lower_wick:
        bearish_high_wave_candle = True
        output += f"Bearish High Wave Candle pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_hikkake = False

for i in range(3, len(data)):
    # Check for higher highs and higher lows
    is_higher_highs = data['High'][i] > data['High'][i-1] and data['Low'][i] > data['Low'][i-1]
    is_higher_lows = data['Low'][i] > data['Low'][i-2]
    
    # Check for a smaller inside candlestick followed by a bearish candlestick breaking below the inside candlestick's low
    is_inside_candlestick = data['High'][i-1] < data['High'][i] and data['Low'][i-1] < data['Low'][i]
    is_bearish_breakout = data['Close'][i] < data['Low'][i-1]
    
    if is_higher_highs and is_higher_lows and is_inside_candlestick and is_bearish_breakout:
        bearish_hikkake = True
        output += f"Bearish Hikkake pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_modified_hikkake = False

for i in range(3, len(data)):
    # Check for higher highs and higher lows
    is_higher_highs = data['High'][i] > data['High'][i-1] and data['Low'][i] > data['Low'][i-1]
    is_higher_lows = data['Low'][i] > data['Low'][i-2]
    
    # Check for a smaller inside candlestick followed by a bearish candlestick breaking below the inside candlestick's low
    is_inside_candlestick = data['High'][i-1] > data['High'][i] and data['Low'][i-1] < data['Low'][i]
    is_bearish_breakout = data['Close'][i] < data['Low'][i-1]
    
    if is_higher_highs and is_higher_lows and is_inside_candlestick and is_bearish_breakout:
        bearish_modified_hikkake = True
        output += f"Bearish Modified Hikkake pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_opening_marubozu = False

for i in range(1, len(data)):
    # Check for a long bearish candlestick with no or very small shadows
    is_bearish_marubozu = data['Open'][i] > data['Close'][i] and (data['Open'][i] - data['Low'][i]) / (data['High'][i] - data['Low'][i]) > 0.9
    
    if is_bearish_marubozu:
        bearish_opening_marubozu = True
        output += f"Bearish Opening Marubozu pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_concealing_baby_swallow = False

for i in range(4, len(data)):
    # Check for the first four bullish candlesticks
    are_bullish_1_4 = all(data['Close'][i-j] > data['Open'][i-j] for j in range(4, 0, -1))
    
    # Check for a doji or small bullish candlestick as the third candlestick
    is_doji_or_small_bullish = data['Open'][i-2] < data['Close'][i-2] and (data['Close'][i-2] - data['Open'][i-2]) / (data['High'][i-2] - data['Low'][i-2]) < 0.1
    
    # Check for a bearish candlestick that engulfs the previous bullish candlesticks as the fifth candlestick
    is_bearish_5 = data['Open'][i] > data['Close'][i-1] and data['Close'][i] < data['Open'][i-1] and data['Close'][i] < data['Open'][i-2] and data['Open'][i] > data['Close'][i-3]
    
    if are_bullish_1_4 and is_doji_or_small_bullish and is_bearish_5:
        bearish_concealing_baby_swallow = True
        output += f"Bearish Concealing Baby Swallow pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_three_line_strike = False

for i in range(3, len(data)):
    # Check for the first three bullish candlesticks
    are_bullish_1_3 = all(data['Close'][i-j] > data['Open'][i-j] for j in range(3, 0, -1))
    
    # Check for the fourth bearish candlestick that gaps down below the low of the third bullish candlestick
    is_bearish_4 = data['Open'][i] < data['Low'][i-3] and data['Close'][i] < data['Open'][i-3]
    
    if are_bullish_1_3 and is_bearish_4:
        bearish_three_line_strike = True
        output += f"Bearish Three-Line Strike pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_three_method_formation = False

for i in range(4, len(data)):
    # Check for the first bullish candlestick
    is_bullish_1 = data['Close'][i-4] > data['Open'][i-4]
    
    # Check for the three small bearish candlesticks contained within the range of the first bullish candlestick
    are_bearish_2_4 = all(data['Open'][i-j] > data['Low'][i-4] and data['Close'][i-j] < data['High'][i-4] for j in range(3, 0, -1))
    
    # Check for the fifth bearish candlestick that closes below the range of the first bullish candlestick
    is_bearish_5 = data['Close'][i] < data['Low'][i-4]
    
    if is_bullish_1 and are_bearish_2_4 and is_bearish_5:
        bearish_three_method_formation = True
        output += f"Bearish Three-Method Formation pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_falling_three_methods = False

for i in range(4, len(data)):
    # Check for the first bullish candlestick
    is_bullish_1 = data['Close'][i-4] > data['Open'][i-4]
    
    # Check for the three small bearish candlesticks contained within the range of the first bullish candlestick
    are_bearish_2_4 = all(data['Open'][i-j] > data['Low'][i-4] and data['Close'][i-j] < data['High'][i-4] for j in range(3, 0, -1))
    
    # Check for the fifth bearish candlestick that closes below the range of the first bullish candlestick
    is_bearish_5 = data['Close'][i] < data['Low'][i-4]
    
    if is_bullish_1 and are_bearish_2_4 and is_bearish_5:
        bearish_falling_three_methods = True
        output += f"Bearish Falling Three Methods pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_deliberation = False

for i in range(2, len(data)):
    # Check for the first two bullish candlesticks with small real bodies and overlap
    is_bullish_1 = (data['Close'][i-2] > data['Open'][i-2]) and ((data['Close'][i-2] - data['Open'][i-2]) / (data['High'][i-2] - data['Low'][i-2]) < 0.2)
    is_bullish_2 = (data['Close'][i-1] > data['Open'][i-1]) and ((data['Close'][i-1] - data['Open'][i-1]) / (data['High'][i-1] - data['Low'][i-1]) < 0.2)
    are_bullish_overlap = (data['High'][i-2] > data['High'][i-1]) and (data['Low'][i-2] < data['Low'][i-1])
    
    # Check for the third bearish candlestick that engulfs the previous two bullish candlesticks
    is_bearish_3 = (data['Open'][i] > data['Close'][i]) and (data['Open'][i] < data['Close'][i-2]) and (data['Close'][i] > data['Open'][i-1]) and (data['Close'][i] > data['Open'][i-2])
    
    if is_bullish_1 and is_bullish_2 and are_bullish_overlap and is_bearish_3:
        bearish_deliberation = True
        output += f"Bearish Deliberation pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_thrusting = False

for i in range(1, len(data)):
    # Check for a large bullish candlestick
    is_large_bullish = (data['Close'][i-1] > data['Open'][i-1]) and \
                       ((data['Close'][i-1] - data['Open'][i-1]) > (0.5 * (data['High'][i-1] - data['Low'][i-1])))
    # Check for a smaller bearish candlestick
    is_smaller_bearish = (data['Open'][i] > data['Close'][i-1]) and \
                         (data['Close'][i] < ((data['Open'][i-1] + data['Close'][i-1]) / 2))
    
    if is_large_bullish and is_smaller_bearish:
        bearish_thrusting = True
        output += f"Bearish Thrusting pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_ladder_top = False

for i in range(3, len(data)):
    # Check for ascending candlesticks
    is_ascending = all(data['Close'][i-j] > data['Close'][i-j-1] for j in range(3))
    # Check for small real bodies and small or nonexistent shadows
    is_small_candles = all((data['Open'][i-j] < data['Close'][i-j]) and
                           (abs(data['Open'][i-j] - data['Close'][i-j]) < (0.1 * (data['High'][i-j] - data['Low'][i-j]))) for j in range(3))
    # Check for larger bearish engulfing candlestick
    is_bearish_engulfing = (data['Open'][i] > data['Close'][i-3]) and \
                           (data['Close'][i] < data['Open'][i-3]) and \
                           (data['Open'][i] > data['Close'][i-2]) and \
                           (data['Close'][i] < data['Open'][i-2]) and \
                           (data['Open'][i] > data['Close'][i-1]) and \
                           (data['Close'][i] < data['Open'][i-1]) and \
                           (data['Open'][i] > data['Close'][i-4]) and \
                           (data['Close'][i] < data['Open'][i-4])

    if is_ascending and is_small_candles and is_bearish_engulfing:
        bearish_ladder_top = True
        output += f"Bearish Ladder Top pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Three Mountain Top pattern
bearish_three_mountain_top = False
for i in range(5, len(data)-5):
    if (data['High'][i] > data['High'][i-1] and data['High'][i-1] > data['High'][i-2]
    and data['High'][i-2] > data['High'][i-3] and data['High'][i-3] > data['High'][i-4]
    and data['High'][i-4] < data['High'][i-5] and data['Low'][i] < data['Low'][i-1]
    and data['Low'][i-1] < data['Low'][i-2] and data['Low'][i-2] < data['Low'][i-3]
    and data['Low'][i-3] < data['Low'][i-4] and data['Low'][i-4] > data['Low'][i-5]):
        bearish_three_mountain_top = True
        output += f"Bearish Three Mountain Top pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Downside Gap Three Methods pattern
bearish_downside_gap_three_methods = False
for i in range(3, len(data)-3):
    if (data['Open'][i] > data['Close'][i]
    and data['Close'][i] < data['Open'][i-1] and data['Open'][i-1] < data['Close'][i-1]
    and data['Close'][i-1] < data['Open'][i-2] and data['Open'][i-2] < data['Close'][i-2]
    and data['Close'][i-2] < data['Open'][i-3] and data['Open'][i-3] < data['Close'][i-3]
    and data['Open'][i-1] > data['Close'][i-3] and data['Open'][i] > data['Close'][i-3]):
        bearish_downside_gap_three_methods = True
        output += f"Bearish Downside Gap Three Methods pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Inverted Hammer pattern
bearish_inverted_hammer = False
for i in range(1, len(data)-1):
    if (data['High'][i] < data['Open'][i] and data['High'][i] < data['Close'][i]
    and abs(data['Open'][i] - data['Close'][i]) <= 0.1 * (data['High'][i-1] - data['Low'][i-1])
    and data['Open'][i-1] < data['Close'][i-1]):
        bearish_inverted_hammer = True
        output += f"Bearish Inverted Hammer pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Shooting Star pattern
bearish_shooting_star = False
for i in range(1, len(data)-1):
    if (data['High'][i-1] < data['Open'][i-1] and data['Open'][i-1] > data['Close'][i-1]
    and data['High'][i] < data['Open'][i] and data['Open'][i] > data['Close'][i]
    and abs(data['Open'][i-1] - data['Close'][i-1]) >= 2 * abs(data['Open'][i] - data['Close'][i])
    and data['Close'][i] < data['Close'][i-1]):
        bearish_shooting_star = True
        output += f"Bearish Shooting Star pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Morning Star pattern
bearish_morning_star = False
for i in range(2, len(data)-2):
    if (data['Close'][i] > data['Open'][i] and abs(data['Open'][i] - data['Close'][i]) < abs(data['Open'][i-1] - data['Close'][i-1]) and data['Open'][i-1] > data['Close'][i-1]
    and data['Open'][i-2] < data['Close'][i-2]):
        bearish_morning_star = True
        output +=f"Bearish Morning Star pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Harami Cross pattern
bearish_harami_cross = False
for i in range(1, len(data)-1):
    if data['Close'][i] > data['Open'][i] and abs(data['Open'][i] - data['Close'][i]) < abs(data['Open'][i-1] - data['Close'][i-1]) and data['Open'][i-1] > data['Close'][i-1]:
        bearish_harami_cross = True
        output += f"Bearish Harami Cross pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Kicker pattern
bearish_kicker = False
for i in range(1, len(data)-1):
    if data['Close'][i] > data['Open'][i] and data['Close'][i-1] < data['Open'][i-1] and data['Open'][i] < data['Close'][i-1]:
        bearish_kicker = True
        output += f"Bearish Kicker pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Meeting Lines pattern
bearish_meeting_lines = False
for i in range(1, len(data)-1):
    if data['Close'][i] > data['Open'][i] and data['High'][i] >= data['High'][i-1] and data['Low'][i] <= data['Low'][i-1]:
        bearish_meeting_lines = True
        output  += f"Bearish Meeting Lines pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Separating Lines pattern
bearish_separating_lines = False
for i in range(1, len(data)-1):
    if data['Close'][i] > data['Open'][i] and data['Open'][i-1] > data['Close'][i-1] and data['Close'][i] < data['Open'][i-1]:
        bearish_separating_lines = True
        output += f"Bearish Separating Lines pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Thrust pattern
bearish_thrust = False
for i in range(1, len(data)-1):
    if data['Close'][i] > data['Open'][i] and data['Close'][i-1] < data['Open'][i-1] and data['Close'][i] < data['Open'][i-1]:
        bearish_thrust = True
        output += f"Bearish Thrust pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Belt Hold pattern
bearish_belt_hold = False
for i in range(1, len(data)-1):
    if data['Open'][i] > data['Close'][i] and data['Open'][i] == data['High'][i] and data['Open'][i] == data['Low'][i] and data['Open'][i] == data['Close'][i-1] and data['Close'][i] < data['Open'][i-1]:
        bearish_belt_hold = True
        output += f"Bearish Belt Hold pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

bearish_homing_pigeon = False
for i in range(1, len(data)-1):
    if data['Open'][i] > data['Close'][i] and data['Open'][i-1] < data['Close'][i-1] and data['Open'][i] < data['Open'][i-1] and data['Close'][i] < data['Open'][i]:
        bearish_homing_pigeon = True
        output += f"Bearish Homing Pigeon pattern identified at date: {data['Date'][i]}\n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Stalled Pattern
bearish_stalled = False
for i in range(1, len(data)-1):
    if data['Open'][i] == data['Close'][i] and data['Open'][i-1] < data['Close'][i-1] and data['Open'][i] < data['Open'][i-1]:
        bearish_stalled = True
        output += f"Bearish Stalled Pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Kicking pattern
bearish_kicking = False
for i in range(1, len(data)-1):
    if data['Open'][i] > data['Close'][i] and data['Open'][i-1] < data['Close'][i-1] and data['Open'][i] < data['Open'][i-1] and data['Close'][i] < data['Open'][i]:
        bearish_kicking = True
        output += f"Bearish Kicking pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()


# Bearish Closing Marubozu pattern
bearish_closing_marubozu = False
for i in range(1, len(data)-1):
    if data['Open'][i] < data['Close'][i] and data['Close'][i] < data['Low'][i] and data['Open'][i] == data['High'][i] and data['Close'][i] == data['Low'][i]:
        bearish_closing_marubozu = True
        output += f"Bearish Closing Marubozu pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Shooting Star Pattern
shooting_star = False
for i in range(len(data)):
    if data['Open'][i] > data['Close'][i] and (data['High'][i] - data['Low'][i]) > 3 * (data['Open'][i] - data['Close'][i]) and (data['High'][i] - data['Close'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        shooting_star = True
        output += f"Shooting Star pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Evening Star Pattern
evening_star = False
for i in range(2, len(data)-2):
    if data['Close'][i-2] < data['Open'][i-2] and abs(data['Close'][i-1] - data['Open'][i-1]) < 0.1 * (data['High'][i-1] - data['Low'][i-1]) and data['Open'][i] > data['Close'][i] and (data['Open'][i] - data['Close'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6 and (data['Close'][i+1] - data['Open'][i+1]) / (0.001 + data['High'][i+1] - data['Low'][i+1]) > 0.6 and data['Close'][i+2] < data['Open'][i+2]:
        evening_star = True
        output += f"Evening Star pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Identify Double Top pattern
double_top = False
for i in range(1, len(data)-1):
    if data['Close'][i] > data['Close'][i-1] and data['Close'][i] > data['Close'][i+1]:
        double_top = True
        output += f"Double Top pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Dark Cloud Cover Pattern
bearish_dark_cloud_cover = False
for i in range(1, len(data)-1):
    if data['Close'][i-1] > data['Open'][i-1] and data['Open'][i] > data['Close'][i] and data['Close'][i] < 0.5 * (data['Open'][i-1] + data['Close'][i-1]) and data['Close'][i] > data['Open'][i-1]:
        bearish_dark_cloud_cover = True
        output += f"Bearish Dark Cloud Cover pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Identify Bear Flag pattern
bear_flag = False
for i in range(1, len(data)-1):
    if data['High'][i] < data['High'][i-1] and data['Low'][i] > data['Low'][i+1] and data['Open'][i] > data['Close'][i] and data['Open'][i+1] < data['Close'][i] and data['Close'][i+1] < data['Open'][i]:
        bear_flag = True
        output += f"Bear Flag pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Hanging Man Pattern
bearish_hanging_man = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]) and data['Open'][i] > data['Close'][i] and (data['Open'][i] - data['Low'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        bearish_hanging_man = True
        output += f"Bearish Hanging Man pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Evening Star Pattern
bearish_evening_star = False
for i in range(2, len(data)-2):
    if data['Open'][i-2] < data['Close'][i-2] and data['Open'][i-1] < data['Close'][i-1] and data['Close'][i] < data['Open'][i] and (data['Open'][i] - data['Close'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6 and data['Close'][i-2] > data['Close'][i-1] and data['Open'][i] > data['Close'][i-2]:
        bearish_evening_star = True
        output += f"Bearish Evening Star pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Shooting Star Pattern
bearish_shooting_star = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]) and data['Open'][i] > data['Close'][i] and (data['High'][i] - data['Open'][i]) / (0.001 + data['High'][i] - data['Low'][i]) > 0.6:
        bearish_shooting_star = True
        output += f"Bearish Shooting Star pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Harami Pattern
bearish_harami = False
for i in range(1, len(data)-1):
    if data['Open'][i] < data['Close'][i] and data['Open'][i] > data['Close'][i-1] and data['Close'][i] < data['Open'][i-1] and data['Open'][i] > data['Close'][i-1]:
        bearish_harami = True
        output += f"Bearish Harami pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()


bearish_doji = False
for i in range(len(data)):
    if abs(data['Close'][i] - data['Open'][i]) < 0.1 * (data['High'][i] - data['Low'][i]) and data['Close'][i] < data['Open'][i]:
        bearish_doji = True
        output += f"Bearish Doji pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Engulfing Pattern
bearish_engulfing = False
for i in range(1, len(data)-1):
    if data['Open'][i] < data['Close'][i] and data['Close'][i-1] < data['Open'][i-1] and data['Close'][i] < data['Open'][i-1] and data['Open'][i] > data['Close'][i-1]:
        bearish_engulfing = True
        output += f"Bearish Engulfing pattern identified at date: {data['Date'][i]} \n"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

# Bearish Deliberation pattern
bearish_deliberation = False
for i in range(2, len(data)-2):
    if data['Open'][i] > data['Open'][i-1] and data['Open'][i] < data['Open'][i+1] and data['Open'][i] > data['Close'][i-1] and data['Open'][i] < data['Close'][i-2]:
        bearish_deliberation = True
        output += f"Bearish Deliberation pattern identified at date: {data['Date'][i]}"
        break
if len([c for c in output if c.isalpha()]) > 5:
    print("there are signal to buy ")
        # Create a Tkinter window
    window = tk.Tk()
    window.title("the doctor recogniz some patherns give a look...")
    window.configure(bg='black')  # Set window background color to black

    # Create a Text widget to display the output
    output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
    output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

    # Define a function to append text to the output Text widget with bold style
    def append_output(text):
        output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
        output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
        output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
        output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

    # Call the append_output function to append your code's output to the Text widget
    # Replace the following lines with your own code that generates output
    append_output(output)

    # Start the Tkinter event loop
    window.mainloop()
    sys.exit()

    
#bon part#############################################################################
    stocksymbols = ['pltr']
    startdate = date(2022, 1,1)
    end_date = date.today() - timedelta(days=1)
    dataframe = yf.download(tickers=stocksymbols, period='1mo', index_as_date=True, interval='5d')
    areaDataframe = yf.download(tickers=stocksymbols[0], period='1d', interval='5m')
    def getMyPortfolio(stocks = stocksymbols ,start = startdate , end = end_date):
        data = web.get_data_yahoo(stocks, start = startdate ,end= end_date )
        return data
    #SMA BUY SELL
    #Function for buy and sell signal
    def buy_sell(data):
        signalBuy = []
        signalSell = []
        position = False

        for i in range(len(data)):
            if data['SMA 20'][i] > data['SMA 100'][i]:
                if position == False :
                    signalBuy.append(data['Adj Close'][i])
                    signalSell.append(np.nan)
                    position = True
                else:
                    signalBuy.append(np.nan)
                    signalSell.append(np.nan)
            elif data['SMA 20'][i] < data['SMA 100'][i]:
                if position == True:
                    signalBuy.append(np.nan)
                    signalSell.append(data['Adj Close'][i])
                    position = False
                else:
                    signalBuy.append(np.nan)
                    signalSell.append(np.nan)
            else:
                signalBuy.append(np.nan)
                signalSell.append(np.nan)
        return pd.Series([signalBuy, signalSell])

    def calculate_shortEMA(dataframe):
        ShortEMA = dataframe.Close.ewm(span=12, adjust=False).mean()
        return ShortEMA

    def calculate_longEMA(dataframe):
            LongEMA = dataframe.Close.ewm(span=26, adjust=False).mean()
            return LongEMA
        
    def calculate_MACD(dataframe):
            MACD = calculate_longEMA(dataframe) - calculate_shortEMA(dataframe)
            return MACD

    def computeRSI (data, time_window):
        diff = data.diff(1).dropna()
        up_chg = 0 * diff
        down_chg = 0 * diff
        up_chg[diff > 0] = diff[ diff>0 ]
        down_chg[diff < 0] = diff[ diff < 0 ]
        up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
        down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
        rs = abs(up_chg_avg/down_chg_avg)
        rsi = 100 - 100/(1+rs)
        return rsi

    def epsCalc(symbol):
        #get info
        symbolData = yf.Ticker(symbol).earnings_history
        count = 0
        epsLst= []
        epsGrowth = 0
        #delete all cols that are not nec
        del symbolData['Symbol']
        del symbolData['Company']
        del symbolData['Surprise(%)']
        
        #find what is the last qurt to show actual eps
        i = 0
        while isnan(symbolData['Reported EPS'][i]):
            count += 1
            i += 1

        #delete all of the rows that are not the last to one ear ago of eps
        for i in range(count):
            symbolData = symbolData.drop(i)
        for i in range(count+5, len(symbolData) - 1 + 5):
            symbolData = symbolData.drop(i)
        
        #delete all but the last and four qurt ago eps
        for i in range(count + 1, len(symbolData) - 1 + 4):
            symbolData = symbolData.drop(i)
        
        for i in symbolData['Reported EPS']:
            epsLst.append(i)
        
        epsGrowth = (epsLst[0]/epsLst[1] - 1)*100
        return (epsLst[0] , epsGrowth)



    def getTweetsSummery(symbol):
        summery = []
        colms = ["Negative", "Positive", "Up", "Down", "Plus", "Minus", "None", "Number of Tweets"]
        limit = (datetime.now().replace(tzinfo=timezone.utc) - timedelta(hours=24))

        Negative = 0
        Positive = 0
        Up = 0
        Down = 0
        Plus = 0
        Minus = 0
        count = 0

        for tweet in snt.TwitterHashtagScraper(f'${symbol}').get_items():
            if tweet.date < limit:
                break
            else:
                count += 1
                if tweet.content.find('NEGATIVE') != -1:
                    Negative += 1
                if tweet.content.find('POSITIVE') != -1:
                    Positive += 1
                if tweet.content.find('UP') != -1:
                    Up += 1
                if tweet.content.find('DOWN') != -1:
                    Down += 1
                if tweet.content.find('+') != -1:
                    Plus += 1
                if tweet.content.find('-') != -1:
                    Minus += 1
        summery = [Negative, Positive, Up, Down, Plus, Minus, count - (Negative + Positive + Up + Down + Plus + Minus), count]
        return pd.DataFrame([summery], columns=colms)

    def putsVolume(symbol):
        lst = []
        data = yf.Ticker(stocksymbols[0]).option_chain().puts
        for i in data['volume']:
            lst.append(i)
        return pd.DataFrame(data.loc[lst.index(max(lst))])

    def callsVolume(symbol):
        lst = []
        data = yf.Ticker(stocksymbols[0]).option_chain().calls
        for i in data['volume']:
            lst.append(i)
        return pd.DataFrame(data.loc[lst.index(max(lst))])

    def getAreaOfGraph(symbol):
        dff = areaDataframe

        del dff['Adj Close']
        del dff['High']
        del dff['Low']
        del dff['Open']
        del dff['Volume']

        new_df = dff.to_dict()['Close']
        y = []
        for time in new_df:
            y.append(new_df[time])
        
        y_sum = y[0] + y[len(y) - 1]
        middle_part = 0.0
        for i in range(1,len(y)-1):
            middle_part += y[i]
        
        y_sum += 2 * middle_part

        return y_sum * 5 * 0.5

    def main():
        bon = 0
        allVol = 0
        plt.style.use('fivethirtyeight')
        yf.pdr_override()
        data = getMyPortfolio(stocksymbols)
        ticker_df = data.reset_index()
        
        df = ticker_df

        area = getAreaOfGraph(stocksymbols[0])

        df['RSI'] = computeRSI(df['Adj Close'], 14)

        data['SMA 20'] = ta.sma(data['Close'],20)
        data['SMA 100'] = ta.sma(data['Close'],100)
        volume = data['Volume']

        # data['Buy_Signal_price'], data['Sell_Signal_price'] = buy_sell(data)

        lastRsi = df['RSI'][len(df['RSI']) - 1]
        lastSma20 = data['SMA 20'][len(data['SMA 20']) - 1]
        lastSma100 = data['SMA 100'][len(data['SMA 100']) - 1]
        lastPrice = data['Adj Close'][len(data['Adj Close']) - 1]
        lastMacd = calculate_MACD(dataframe)[len(dataframe) - 1]
        lastVolume = volume[len(volume) - 1]

        for i in range(0, len(volume) - 2):
            allVol += volume[i]
        
        allVol = allVol / (len(volume) - 2)

        print ( 'Stock >>> ', stocksymbols[0])
        print (  'Start date >>> ', startdate)
        print (  'End date >>> ', end_date)
        print ( 'RSI >>> ' ,lastRsi)
        print ( 'SMA 20 >>> ' , lastSma20)
        print ( 'SMA 100 >>> ' , lastSma100)
        print ( 'MACD >>> ', lastMacd)
        print ( 'Volume >>> ', lastVolume)
        print ('price >>> ', lastPrice) 

        if lastRsi <= 40:
            bon += 1
        elif 60 >= lastRsi and lastRsi >= 40:
            bon += 0.5
        elif lastRsi >= 60:
            pass

        if ( lastSma100 - lastPrice ) > 0:
            bon += 1
        
        if ( lastSma20 - lastPrice) > 0:
            bon += 1
        
        if lastMacd > 0:
            bon += 1
        elif lastMacd < 0:
            bon -= 1
        
        if lastVolume > allVol:
            bon += 1   
        print('bon >>> ', bon/5)
# Create a Tkinter window
window = tk.Tk()
window.title("the doctor recogniz some patherns give a look...")
window.configure(bg='black')  # Set window background color to black

# Create a Text widget to display the output
output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

# Define a function to append text to the output Text widget with bold style
def append_output(text):
    output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
    output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
    output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
    output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

# Call the append_output function to append your code's output to the Text widget
# Replace the following lines with your own code that generates output
append_output(output)

# Start the Tkinter event loop
window.mainloop()

if __name__ == "__main__":
    main()


#MIT License

#Copyright (c) 2023 Lior Salmanovich

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import tkinter as tk
from PIL import Image, ImageTk
import yahoo_fin.stock_info as si
import yfinance as yf
import subprocess
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

#the list of wich patterns are in the code here: https://docs.google.com/document/d/1_bWSGf4Z-f8H2aXh0miNgLBGqrKnu_y_uCaa02-kb20/edit?usp=sharing
# Read the CSV file
data = pd.read_csv('pltr_stock_data.csv')
output =  "hello \n" 
# Define the stock symbol
stock_symbol = 'AAPL'  # Replace with the desired stock symbol
# Identify Double Bottom pattern
double_bottom = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Close'][i-1] and data['Close'][i] < data['Close'][i+1]:
        double_bottom = True
        output += f"Double Bottom pattern identified at date: {data['Date'][i]} \n"
        
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

for key in selected_keys:
    if key in fundamentals:
        output += f"{key}: {fundamentals[key]}\n"
    else:
        output += f"{key} not available for {stock_symbol}\n"


# Fetch historical data
stock_data = yf.download(stock_symbol, period='1y')

# Calculate the 100-day moving average
stock_data['SMA_100'] = stock_data['Close'].rolling(window=100).mean()

# Get the current price of the stock
current_price = stock_data['Close'].iloc[-1]

# Get the last value of the SMA 100
sma_100_last_value = stock_data['SMA_100'].iloc[-1]

# Calculate the difference between SMA 100 and the current price
x = sma_100_last_value - current_price
###########################################################################
# Define the stock symbol
stock_symbol = 'AAPL'  # Replace with the desired stock symbol

# Fetch historical data
stock_data = yf.download(stock_symbol, period='1y')

# Calculate the 200-day moving average
stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()

# Get the current price of the stock
current_price = stock_data['Close'].iloc[-1]

# Get the last value of the SMA 200
sma_200_last_value = stock_data['SMA_200'].iloc[-1]

# Calculate the difference between SMA 200 and the current price
y = sma_200_last_value - current_price
###########################################################################

# Define the stock symbol
stock_symbol = 'AAPL'  # Replace with the desired stock symbol

# Fetch historical data
stock_data = yf.download(stock_symbol, period='1y')

# Calculate the 200-day moving average
stock_data['SMA_200'] = stock_data['Close'].rolling(window=300).mean()

# Get the current price of the stock
current_price = stock_data['Close'].iloc[-1]

# Get the last value of the SMA 200
sma_300_last_value = stock_data['SMA_200'].iloc[-1]

# Calculate the difference between SMA 200 and the current price
z = sma_300_last_value - current_price
radius = 50  # Define the radius globally
circle_spacing = 50  # Define the spacing between circles

def update_circles(value1, value2, value3):
    canvas.delete("circle")  # Clear previous circles (if any)
    
    y = 150  # Y-coordinate of the circle's center
    
    draw_circle(value1, 90, 100, "sma 100")
    draw_circle(value2, 210, 110, "sma 200")
    draw_circle(value3, 330, 120, "sma 300")

def draw_circle(value, x, y, text):
    # Set default color to black for the middle and edges
    circle_color = "black"
    text_color = "black"
    
    if value < 0:
        text_color = "red"
    else:
        text_color = "green"
    
    # Draw the middle of the circle in black
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black", outline="black", tags="circle_middle")
    # Draw the edge of the circle in red or green
    canvas.create_oval(x - radius + 5, y - radius + 5, x + radius - 5, y + radius - 5, fill=circle_color, outline=text_color, tags="circle_edge")
    # Draw the user-defined text in the middle of the circle
    canvas.create_text(x, y, text=text, fill="white", font=("Helvetica", 12, "bold"))



# Create a Tkinter window
window = tk.Tk()
window.title("Integrated Visualization")
window.configure(bg='black')

# Create a canvas to draw on
canvas = tk.Canvas(window, width=400, height=200)  # Adjust the width and height as needed
canvas.grid(row=1, column=0, columnspan=1)

# Create a Text widget to display the output
output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD, height=10)  # Adjust the height as needed
output_text.grid(row=10, column=0, columnspan=2)

# Define a function to append text to the output Text widget with bold style
def append_output(text):
    output_text.configure(state=tk.NORMAL)
    output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))
    output_text.insert(tk.END, text, "bold")
    output_text.configure(state=tk.DISABLED)

# Append your code's output to the Text widget
append_output(output)

# Update the circles with predefined values
update_circles(x, y, z)

# Start the Tkinter event loop
window.mainloop()




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
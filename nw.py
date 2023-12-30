import tkinter as tk
from PIL import Image, ImageTk
import yahoo_fin.stock_info as si
import yfinance as yf
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Define the stock symbol
stock_symbol = 'AAPL'  # Replace with the desired stock symbol

# Read the CSV file
data = pd.read_csv('pltr_stock_data.csv')
output = "hello \n"

# Identify Double Bottom pattern
double_bottom = False
for i in range(1, len(data)-1):
    if data['Close'][i] < data['Close'][i-1] and data['Close'][i] < data['Close'][i+1]:
        double_bottom = True
        output += f"Double Bottom pattern identified at date: {data['Date'][i]} \n"

# Fetch specific fundamental financial information
stock = yf.Ticker(stock_symbol)
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

# Calculate the moving averages
stock_data['SMA_100'] = stock_data['Close'].rolling(window=100).mean()
stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()
stock_data['SMA_300'] = stock_data['Close'].rolling(window=300).mean()

# Calculate the difference between SMA and current price
current_price = stock_data['Close'].iloc[-1]
sma_100_last_value = stock_data['SMA_100'].iloc[-1]
sma_200_last_value = stock_data['SMA_200'].iloc[-1]
sma_300_last_value = stock_data['SMA_300'].iloc[-1]

x = sma_100_last_value - current_price
y = sma_200_last_value - current_price
z = sma_300_last_value - current_price

# Create a Tkinter window
window = tk.Tk()
window.title("Integrated Visualization")
window.configure(bg='black')



# Create a canvas to draw on
canvas = tk.Canvas(window, width=400, height=200)  # Adjust the width and height as needed
canvas.grid(row=1, column=0, columnspan=3)

# Create a FigureCanvasTkAgg widget to display the live stock chart
figure = plt.Figure(figsize=(6, 4), dpi=100)
subplot = figure.add_subplot(1, 1, 1)
subplot.set_title(f"Live Chart for {stock_symbol}")
subplot.set_xlabel("Time")
subplot.set_ylabel("Price")
canvas_widget = FigureCanvasTkAgg(figure, master=window)
canvas_widget.get_tk_widget().grid(row=2, column=0, columnspan=3)

# Create a Text widget to display the output
output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD, height=10)  # Adjust the height as needed
output_text.grid(row=3, column=0, columnspan=3)

# Define a function to append text to the output Text widget with bold style
def append_output(text):
    output_text.configure(state=tk.NORMAL)
    output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))
    output_text.insert(tk.END, text, "bold")
    output_text.configure(state=tk.DISABLED)

# Append your code's output to the Text widget
append_output(output)
radius = 50
# Update the circles with predefined values
def update_circles():
    canvas.delete("circle")  # Clear previous circles (if any)

    y = 150  # Y-coordinate of the circle's center

    draw_circle(x, 90, 100, "sma 100")
    draw_circle(y, 210, 110, "sma 200")
    draw_circle(z, 330, 120, "sma 300")

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

# Start updating the live chart
def update_live_chart():
    stock_data_latest = yf.download(stock_symbol, period='1d', interval='1m')
    subplot.clear()
    subplot.plot(stock_data_latest['Close'])
    subplot.set_title(f"Live Chart for {stock_symbol}")
    subplot.set_xlabel("Time")
    subplot.set_ylabel("Price")
    canvas_widget.draw()
    window.after(60000, update_live_chart)  # Update every minute (adjust as needed)

# Call the update_live_chart function to start updating the live chart
update_live_chart()

# Update the circles with predefined values
update_circles()

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
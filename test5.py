import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

output = ""
for key in selected_keys:
    if key in fundamentals:
        output += f"{key}: {fundamentals[key]}\n"
    else:
        output += f"{key} not available for {stock_symbol}\n"

# Fetch historical data for live chart
stock_data = yf.download(stock_symbol, period='1d', interval='1m')

# Create a Tkinter window
window = tk.Tk()
window.title("Integrated Visualization")
window.configure(bg='black')

# Create a Matplotlib figure for the live stock chart
figure = plt.Figure(figsize=(6, 3), dpi=100)
ax = figure.add_subplot(1, 1, 1)
line, = ax.plot([], [])

# Create a FigureCanvasTkAgg widget to display the Matplotlib figure
canvas_widget = FigureCanvasTkAgg(figure, master=window)
canvas_widget.get_tk_widget().pack()

# Function to update the live stock chart
def update_chart():
    stock_data = yf.download(stock_symbol, period='1d', interval='1m')
    ax.clear()
    ax.plot(stock_data.index, stock_data['Close'], label=stock_symbol)
    ax.legend()
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.set_title('Live Stock Price Chart')
    canvas_widget.draw()
    canvas_widget.get_tk_widget().after(60000, update_chart)  # Update every 1 minute

# Call the update_chart function to start updating the live chart
update_chart()

# Create a Text widget to display the fundamental financial information
output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD, height=10)  # Adjust the height as needed
output_text.pack()

# Append your code's output to the Text widget
output_text.insert(tk.END, output)

# Start the Tkinter event loop
window.mainloop()

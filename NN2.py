import yfinance as yf
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Define the stock symbol and fetch historical data
stock_symbol = 'AAPL'
stock_data = yf.download(stock_symbol, period='1y')

# Preprocess and prepare features and labels
# For simplicity, let's assume you want to predict if the stock price will go up (1) or down (0)
stock_data['Price_Up'] = (stock_data['Close'] < stock_data['Close'].shift(-1)).astype(int)

# Select features and labels
features = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].values
labels = stock_data['Price_Up'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Build a simple neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')

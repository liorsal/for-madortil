import yfinance as yf
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Define the stock symbol and fetch historical data
stock_symbol = 'AAPL'
stock_data = yf.download(stock_symbol, period='1y',interval='1d')

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
print(f'Test accuracy for stock price direction: {test_acc:.4f}')

# Identify Double Bottom pattern
double_bottom_accuracy = 0
for i in range(1, len(stock_data)-1):
    if stock_data['Close'][i] < stock_data['Close'][i-1] and stock_data['Close'][i] < stock_data['Close'][i+1]:
        double_bottom = True
        # Prepare input data for the neural network
        input_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].iloc[i].values.reshape(1, -1)
        # Predict if the stock price will go up
        prediction = model.predict(input_data)
        # Convert prediction to 1 (up) or 0 (down)
        predicted_direction = 1 if prediction > 0.5 else 0
        actual_direction = stock_data['Price_Up'].iloc[i]
        if predicted_direction == actual_direction:
            double_bottom_accuracy += 1

# Calculate and print accuracy of Double Bottom pattern
accuracy = double_bottom_accuracy / len(stock_data)
print(f'Accuracy of Double Bottom pattern for stock price direction: {accuracy:.4f}')

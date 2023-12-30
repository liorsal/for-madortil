import yfinance as yf
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Define the stock symbol and fetch historical data
stock_symbol = 'AAPL'
stock_data = yf.download(stock_symbol, period='1y',interval='1d')

# Reset the index to make 'Date' a regular column
stock_data = stock_data.reset_index()

output = ''
double_bottom = False
for i in range(1, len(stock_data) - 3):  # Adjust the range to avoid going out of bounds
    if (
        stock_data['Close'][i] < stock_data['Close'][i - 1] and
        stock_data['Close'][i] < stock_data['Close'][i + 1] and
        stock_data['Close'][i + 2] < stock_data['Close'][i + 3]
    ):
        output += f"Double Bottom pattern identified at date: {stock_data['Date'][i]} \n"

        double_bottom = True



# Create a function to evaluate the Double Bottom pattern recognition accuracy

if double_bottom :
    # Preprocess and prepare features and labels for the stock price direction prediction
    stock_data['Price_Up'] = (stock_data['Open'] < stock_data['Open'].shift(-1)).astype(int)
    features = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].values
    labels = stock_data['Price_Up'].values
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Create a function to train the machine learning model
    def train_model(X_train, y_train, X_test, y_test):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(5,)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
        return model

    # Initial training of the model
    model = train_model(X_train, y_train, X_test, y_test)

    def evaluate_double_bottom_accuracy(model, stock_data):
        double_bottom_accuracy = 0
        for i in range(1, len(stock_data) - 1):
            if stock_data['Close'][i] < stock_data['Close'][i - 1] and stock_data['Close'][i] < stock_data['Close'][i + 1]:
                double_bottom = True
                input_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].iloc[i].values.reshape(1, -1)
                prediction = model.predict(input_data)
                predicted_direction = 1 if prediction > 0.5 else 0
                actual_direction = stock_data['Price_Up'].iloc[i]
                if predicted_direction == actual_direction:
                    double_bottom_accuracy += 1
        return double_bottom_accuracy / len(stock_data)

# Set an initial threshold for accuracy
accuracy_threshold = 0

# Continuously evaluate accuracy and retrain the model until it meets the threshold
while True:
    current_accuracy = evaluate_double_bottom_accuracy(model, stock_data)
    print(f'Current Double Bottom pattern accuracy: {current_accuracy:.4f}')
    
    if current_accuracy < accuracy_threshold:
        print('Retraining the model...')
        model = train_model(X_train, y_train, X_test, y_test)
    else:
        print('Accuracy threshold met. Exiting...' , len(stock_data) , output)
        break

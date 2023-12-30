import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load the data
data = pd.read_csv('synthetic_data.csv')

# Define the features
features = ['close', 'volume']

# Create the target variable
data['is_cup_and_handle'] = data['Pattern'] == 'Cup and Handle'

# Compute the moving averages
data['SMA'] = data['close'].rolling(window=20).mean()
data['EMA'] = data['close'].ewm(span=20, adjust=False).mean()

# Compute the MACD
data['EMA12'] = data['close'].ewm(span=12, adjust=False).mean()
data['EMA26'] = data['close'].ewm(span=26, adjust=False).mean()
data['MACD'] = data['EMA12'] - data['EMA26']

# Compute the RSI
delta = data['close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean().abs()
rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(data[features], data['is_cup_and_handle'], test_size=0.2, random_state=42)

# Scale the features using MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# Train the Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)

# Evaluate the model performance on the validation set
val_preds = rf.predict(X_val_scaled)
val_accuracy = np.mean(val_preds == y_val)
print('Validation Accuracy:', val_accuracy)

# Use the model to make predictions on new data
new_data = pd.read_csv('synthetic_data.csv')
new_data['SMA'] = new_data['close'].rolling(window=20).mean()
new_data['EMA'] = new_data['close'].ewm(span=20, adjust=False).mean()
new_data['EMA12'] = new_data['close'].ewm(span=12, adjust=False).mean()
new_data['EMA26'] = new_data['close'].ewm(span=26, adjust=False).mean()
new_data['MACD'] = new_data['EMA12'] - new_data['EMA26']
delta = new_data['close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean().abs()
rs = avg_gain / avg_loss
new_data['RSI'] = 100 - (100 / (1 + rs))
new_data_scaled = scaler.transform(new_data[features])
new_data_preds = rf.predict(new_data_scaled)
new_data['Pattern'] = np.where(new_data_preds, 'Cup and Handle', 'Not Cup and Handle')

# Print the predicted patterns for new data when Cup and Handle pattern is detected
cup_and_handle_data = new_data[new_data['Pattern'] == 'Cup and Handle']
if not cup_and_handle_data.empty:
    print('Cup and Handle pattern detected in the following data:')
    print(cup_and_handle_data[['close', 'Pattern']])
else:
    print('No Cup and Handle pattern detected in the new data.')

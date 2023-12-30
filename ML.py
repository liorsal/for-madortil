import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import alpaca_trade_api as tradeapi

api = tradeapi.REST('PKF6FQFL86F53UDQ59XU', 'sCIrdCRuPCqTUaFaZQACmqG9lzfiVcwREArNCo6j', base_url='https://paper-api.alpaca.markets')

#the list of which patterns are in the code here: https://docs.google.com/document/d/1_bWSGf4Z-f8H2aXh0miNgLBGqrKnu_y_uCaa02-kb20/edit?usp=sharing
symbol = 'PLTR'
timeframe = '1Min'
limit = 75

# Retrieve bar data from Alpaca
bars = api.get_bars(symbol, timeframe, limit=limit)

# Convert bar data to DataFrame
df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
for bar in bars:
    df = df.append({
        'Date': bar.t,
        'Open': bar.o,
        'High': bar.h,
        'Low': bar.l,
        'Close': bar.c,
        'Adj Close': bar.c,  # no adjustment needed for 1-minute bars
        'Volume': bar.v
    }, ignore_index=True)


######################################bull patters start######################################################################
# Head and Shoulders Pattern Detection
# Define your data, e.g., a pandas DataFrame
data = df.copy()

# Define the features and target
features = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
target = []

# Look for Bullish Head and Shoulders pattern
for i in range(4, len(data)):
    if i >= 4 and \
       data['High'][i-3] < data['High'][i-1] and \
       data['High'][i-2] < data['High'][i-1] and \
       data['High'][i] < data['High'][i-1] and \
       data['Low'][i-3] < data['Low'][i-1] and \
       data['Low'][i-2] < data['Low'][i-1] and \
       data['Low'][i] < data['Low'][i-1]:
        target.append(1)  # 1 denotes an ideal pattern
    else:
        target.append(0)  # 0 denotes a non-ideal pattern

# create the feature matrix and target vector
X = data[features]
y = target

# split the data into training and test sets
if sum(y) == 0:  # check if there are no ideal patterns found
    print("there are No ideal patterns found.")
else:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # train a random forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # make predictions on the test data
    y_pred = clf.predict(X_test)

    # evaluate the model's accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

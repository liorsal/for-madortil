bon = 0
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
allVol = 0
plt.style.use('fivethirtyeight')
yf.pdr_override()
data = pd.read_csv('pltr_stock_data.csv')
ticker_df = data.reset_index()
        
df = ticker_df


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
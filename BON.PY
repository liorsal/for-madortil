import numpy as np
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import pandas_ta as ta
import matplotlib.pyplot as plt
from datetime import date

stocksymbols = ['nflx']
startdate = date(2022, 1, 1)
end_date = date(2022,10,5)
dataframe = yf.download(tickers=stocksymbols, period='1mo', index_as_date=True, interval='5d')

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

def main():
    bon = 0
    plt.style.use('fivethirtyeight')
    yf.pdr_override()

    data = getMyPortfolio(stocksymbols)
    ticker_df = data.reset_index()
    df = ticker_df
    df['RSI'] = computeRSI(df['Adj Close'], 14)

    data['SMA 20'] = ta.sma(data['Close'],20)
    data['SMA 100'] = ta.sma(data['Close'],100)
    volume = data['Volume']

    data['Buy_Signal_price'], data['Sell_Signal_price'] = buy_sell(data)

    lastRsi = df['RSI'][len(df['RSI']) - 1]
    lastSma20 = data['SMA 20'][len(data['SMA 20']) - 1]
    lastSma100 = data['SMA 100'][len(data['SMA 100']) - 1]
    lastPrice = data['Adj Close'][len(data['Adj Close']) - 1]
    lastMacd = calculate_MACD(dataframe)[len(dataframe) - 1]
    lastVolume = volume[len(volume) - 1]

    print('RSI >>> ' ,lastRsi)
    print('SMA 20 >>> ' , lastSma20)
    print('SMA 100 >>> ' , lastSma100)
    print('MACD >>> ', lastMacd)
    print('Volume >>> ', lastVolume)
    print('price >>> ', lastPrice)

    if lastRsi < 40:
        bon += 1
    elif 60 > lastRsi and lastRsi > 40:
        bon += 0.5
    elif lastRsi > 60:
        pass

    if ( lastSma100 - lastPrice ) > 0:
        bon += 1
    
    if ( lastSma20 - lastPrice) > 0:
        bon += 1
    
    if lastMacd > 0:
        bon += 1
    elif lastMacd < 0:
        bon -= 1
    
    allVol = 0
    for i in range(0, len(volume) - 2):
        allVol += volume[i]
    
    allVol = allVol / (len(volume) - 2)
    
    if lastVolume > allVol:
        bon += 1
    
    print('bon >>> ', bon/5)

    '''

    Stock Graph - code

    ig, ax = plt.subplots(figsize=(14,8))
    ax.plot(data['Adj Close'] , label = stocksymbols[0] ,linewidth=1, color='blue', alpha = 0.9)
    ax.plot(data['SMA 4'], label = 'SMA4', alpha = 0.85, linewidth=1)
    ax.plot(data['SMA 14'], label = 'SMA14' , alpha = 0.85, linewidth=1)
    ax.plot(dataframe.index, calculate_MACD(dataframe), label = stocksymbols[0] + ' MACD', color = 'black')
    ax.plot(df['Date'], df['RSI'],label='RSI')
    ax.scatter(data.index , data['Buy_Signal_price'] , label = 'Buy' , marker = '^', color = 'green',alpha =1 )
    ax.scatter(data.index , data['Sell_Signal_price'] , label = 'Sell' , marker = 'v', color = 'red',alpha =1 )
    ax.set_title(stocksymbols[0] + " Price History with buy and sell signals",fontsize=10, backgroundcolor='blue', color='white')
    ax.set_xlabel(f'{startdate} - {end_date}' ,fontsize=10)
    ax.set_ylabel('Close Price INR (%)' , fontsize=10)
    legend = ax.legend()
    ax.grid()
    plt.tight_layout()
    plt.show()
    '''

if __name__ == '_main_':
    main()
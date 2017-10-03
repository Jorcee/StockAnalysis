import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import pandas as pd

with open("Stocks.txt") as file:
    tickers = file.readlines()
for i in range(0,len(tickers)):
    tickers[i] = tickers[i].rstrip()
if '' in tickers:
    del tickers[tickers.index('')]
print(tickers)
myStocks = pd.DataFrame()
for t in tickers:
    myStocks[t] = wb.DataReader(t, data_source='yahoo',start='1995-1-1')['Adj Close']
print(myStocks.head())
daily_returns = (myStocks / myStocks.shift(1)) - 1
for stock in daily_returns:
    stock.plot(figsize(8,5), label='Daily Return')

#PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
#PG['simple_return'].plot(figsize=(8,5), label='Daily Return')
#avg_returns_d = PG['simple_return'].mean()
#avg_returns_d_string = str(round(avg_returns_d, 5) * 100)
#plt.axhline(y=avg_returns_d, color='r', linestyle='-', label='Average Daily Return: ' + avg_returns_d_string)
#plt.ylabel('Percent Daily Return')
#plt.text('2004',-.2, 'Average Daily Return: '+avg_returns_d_string);
plt.legend()
plt.show()
                       

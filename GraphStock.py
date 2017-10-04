import numpy as np
from pandas_datareader import data as wb
import pandas as pd
import matplotlib.pyplot as plt

class GraphStock:
    def graphStock(stockTicker):
        try:
            stock = wb.DataReader(stockTicker.upper(), data_source='yahoo', start='1995-1-1')
        except:
            graphStock(stockTicker)
        stock['simple_return'] =(stock['Adj Close'] / stock['Adj Close'].shift(1)) - 1
        stock['simple_return'].plot(figsize=(8,5), label='Daily Return')
        avg_returns_d = stock['simple_return'].mean()
        avg_returns_d_string = str(round(avg_returns_d, 5) * 100)
        plt.axhline(y=avg_returns_d, color='r', linestyle='-', label='Average Daily Return: ' + avg_returns_d_string)
        plt.ylabel('Percent Daily Return')
        plt.text('2004',-.2, 'Average Daily Return: '+avg_returns_d_string);
        plt.title("Average Daily Returns for " + stockTicker)
        plt.legend()
        plt.show()
        return

    def graphAllStock(stockTickers):
        stocks = pd.DataFrame()
        try:
            for t in stockTickers:
                stocks[t] = wb.DataReader(t.upper().strip('\n'), data_source='yahoo', start='1995-1-1')['Adj Close']
        except:
            graphAllStock(stockTickers)
        (stocks / stocks.iloc[0] * 100).plot(figsize=(8,5))
        plt.title("Normalized Growth Comparison of "+str(stockTickers))
        plt.show()
        return

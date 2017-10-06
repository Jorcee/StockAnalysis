from GraphStock import GraphStock as show
from tkinter import Tk, Label, Button

def addStock(tickers):
    stockToAdd = input("Type the ticker of the stock you would like to add:\n")
    tickers.append(stockToAdd.upper())
    return tickers

def removeStock(tickers):
    stockToRemove = input("Type the ticker of the stock you would like to remove\n")
    tickers.remove(stockToRemove.upper())
    return tickers

def seeStock(tickers):
    stockToSee = input("Type the ticker of the stock you would like to see\n"+
                       "Or type tickers serparated by commas to compare multiple\n" +
                       "Or Type All to see a comparison graph of all\n")
    if stockToSee.lower() == 'all':
        show.graphAllStock(tickers)
    elif "," in stockToSee:
        stockToSee = stockToSee.split(',')
        show.graphAllStock(stockToSee)
    else:
        show.graphStock(stockToSee)
    return

file = open("Stocks.txt","r")
tickers = file.readlines()
file.close()
for i in range(0, len(tickers)):
    tickers[i] = tickers[i].rstrip()
if '' in tickers:
    del tickers[tickers.index('')]
userInput =''
while(userInput.lower() != 'exit'):
    userInput = input("Your stocks are: " + str(tickers) +
                      "\nWhat would you like to do?\n" +
                      "Add,Remove,See,Exit\n")
    if userInput.lower() == "add":
        tickers =  addStock(tickers)
    elif userInput.lower() == "remove":
        tickers = removeStock(tickers)
    elif userInput.lower() == 'see':
        seeStock(tickers)
with open("Stocks.txt",'w') as file:
    for stock in tickers:
        file.write(stock + '\n')
        
exit()







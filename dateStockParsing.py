import pandas as pd
import os
import quandl
import time

authTok = open('auth.txt', 'r').read() # auth token saved locally in txt file
quandl.ApiConfig.api_key = authTok
# data = quandl.get("WIKI/KO", trim_start="2000-12-12", trim_end="2014-12-30")
# print(data["Adj. Close"])

path = "C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/intraQuarter"

def StockPrices():
    df = pd.DataFrame()
    statsPath = path + "/_KeyStats"
    stockList = [x[0] for x in os.walk(statsPath)]

    for eachDir in stockList[1:]:
        try:
            ticker = eachDir.split('\\')[1]
            print(ticker)
            name = "WIKI/"+ticker.upper()
            data = quandl.get(name,
                              trim_start="2000-12-12",
                              trim_end="2014-12-30")
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis=1)
        except Exception as e:
            print(str(e))

    df.to_csv("stock_prices.csv")

StockPrices()



import pandas as pd
import os
import time
from datetime import datetime
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
import re

path = "C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/intraQuarter"
# change according to where intraQuarter folder is stored

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statsPath = path + '/_KeyStats'
    stockList = [x[0] for x in os.walk(statsPath)] # gather all stock names from folder
    #print(stockList)
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'DE Ratio',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference'
                                 'Status'])

    sp500df = pd.read_csv("YAHOO-INDEX_GSPC.csv")
    tickerList = []

    for eachDir in stockList[1:25]:
        eachFile = os.listdir(eachDir)
        ticker = eachDir.split("\\")[1]
        tickerList.append(ticker)

        startingStockValue = False
        startingSP500Value = False

        if len(eachFile) > 0:
            for file in eachFile:
                dateStamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unixTime = time.mktime(dateStamp.timetuple())
                fullPath = eachDir + '/' + file
                source = open(fullPath, 'r').read()
                try:
                    try:
                        value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    except Exception as e:
                        try:
                            value = float(source.split(gather+':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                            #print(str(e), ticker, file)
                        except:
                            value = float(source.split(gather+':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                        #time.sleep(15)
                    try:
                        sp500Date = datetime.fromtimestamp(unixTime).strftime("%Y-%m-%d")
                        row = sp500df[(sp500df["Date"] == sp500Date)]
                        sp500Value = float(row["Adj Close"])
                    except:
                        sp500Date = datetime.fromtimestamp(unixTime-259200).strftime("%Y-%m-%d")
                        row = sp500df[(sp500df["Date"] == sp500Date)]
                        sp500Value = float(row["Adj Close"])
                    try:
                        stockPrice = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                    except Exception as e:
                        try:
                            stockPrice = (source.split("</small><big><b>")[1].split('</b></big>')[0])
                            stockPrice = re.search(r'(\d{1,8}\.\d{1,8})', stockPrice)
                            stockPrice = float(stockPrice.group(1))
                            #print(stockPrice)
                        except Exception as e:
                            stockPrice = (source.split('<span class="time_rtq_ticker"')[1].split('</span>')[0])
                            stockPrice = re.search(r'(\d{1,8}\.\d{1,8})', stockPrice)
                            stockPrice = float(stockPrice.group(1))


                    #print("stock_price:", stockPrice, "ticker:", ticker)

                    if not startingStockValue:
                        startingStockValue = stockPrice
                    if not startingSP500Value:
                        startingSP500Value = sp500Value
                    stockPChange = ((stockPrice - startingStockValue) / startingStockValue) * 100
                    sp500PChange = ((sp500Value - startingSP500Value) / startingSP500Value) * 100

                    difference = stockPChange-sp500PChange
                    if difference>0 :
                        status = 'outperform'
                    else:
                        status = 'underperform'

                    df = df.append({'Date':dateStamp,
                                    'Unix':unixTime,
                                    'Ticker':ticker,
                                    'DE Ratio':value,
                                    'Price':stockPrice,
                                    'stock_p_change':stockPChange,
                                    'SP500':sp500Value,
                                    'sp500_p_change':sp500PChange,
                                    'Difference':difference,
                                    'Status':status}, ignore_index=True)
                except Exception as e:
                    pass
    for eachTicker in tickerList:
        try:
            plotDf = df[(df['Ticker'] == eachTicker)]
            plotDf = plotDf.set_index(['Date'])

            if plotDf['Status'][-1] == "underperform":
                colour = 'r'
            else:
                colour = 'g'

            plotDf['Difference'].plot(label=eachTicker, color = colour)

            plt.legend()
        except:
            pass
    plt.show()
    save = gather.replace(' ', '').replace(')', '').replace('(', '').replace('/','')+'.csv'
    print(save)
    df.to_csv(save)
Key_Stats()




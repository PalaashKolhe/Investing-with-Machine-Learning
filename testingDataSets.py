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

def Key_Stats(gather=["Total Debt/Equity",
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                        'Enterprise Value',
                        'Forward P/E',
                        'PEG Ratio',
                        'Enterprise Value/Revenue',
                        'Enterprise Value/EBITDA',
                        'Revenue',
                        'Gross Profit',
                        'EBITDA',
                        'Net Income Avl to Common ',
                        'Diluted EPS',
                        'Earnings Growth',
                        'Revenue Growth',
                        'Total Cash',
                        'Total Cash Per Share',
                        'Total Debt',
                        'Current Ratio',
                        'Book Value Per Share',
                        'Cash Flow',
                        'Beta',
                        'Held by Insiders',
                        'Held by Institutions',
                        'Shares Short (as of',
                        'Short Ratio',
                        'Short % of Float',
                        'Shares Short (prior ']):
    statsPath = path + '/_KeyStats'
    stockList = [x[0] for x in os.walk(statsPath)] # gather all stock names from folder
    #print(stockList)
    df = pd.DataFrame(columns=['Date',
                               'Unix',
                               'Ticker',
                               'Price',
                               'stock_p_change',
                               'SP500',
                               'sp500_p_change',
                               'Difference',
                               ##############
                               'DE Ratio',
                               'Trailing P/E',
                               'Price/Sales',
                               'Price/Book',
                               'Profit Margin',
                               'Operating Margin',
                               'Return on Assets',
                               'Return on Equity',
                               'Revenue Per Share',
                               'Market Cap',
                               'Enterprise Value',
                               'Forward P/E',
                               'PEG Ratio',
                               'Enterprise Value/Revenue',
                               'Enterprise Value/EBITDA',
                               'Revenue',
                               'Gross Profit',
                               'EBITDA',
                               'Net Income Avl to Common ',
                               'Diluted EPS',
                               'Earnings Growth',
                               'Revenue Growth',
                               'Total Cash',
                               'Total Cash Per Share',
                               'Total Debt',
                               'Current Ratio',
                               'Book Value Per Share',
                               'Cash Flow',
                               'Beta',
                               'Held by Insiders',
                               'Held by Institutions',
                               'Shares Short (as of',
                               'Short Ratio',
                               'Short % of Float',
                               'Shares Short (prior ',
                               ##############
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
                    value_list = []
                    for eachData in gather:
                        try:
                            regex = re.escape(eachData) + r'.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?</td>'
                            value = re.search(regex, source)
                            value = (value.group(1))


                            if "B" in value:
                                value = float(value.replace("B", '')) * 1000000000
                            elif "M" in value:
                                value = float(value.replace("M", '')) * 1000000

                            value_list.append(value)

                        except Exception as e:
                            value = "N/A"
                            value_list.append(value)

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

                    if value_list.count("N/A") > 0:
                        pass
                    else:

                        df = df.append({'Date': dateStamp,
                                        'Unix': unixTime,
                                        'Ticker': ticker,

                                        'Price': stockPrice,
                                        'stock_p_change': stockPChange,
                                        'SP500': sp500Value,
                                        'sp500_p_change': sp500PChange,
                                        'Difference': difference,
                                        'DE Ratio': value_list[0],
                                        # 'Market Cap':value_list[1],
                                        'Trailing P/E': value_list[1],
                                        'Price/Sales': value_list[2],
                                        'Price/Book': value_list[3],
                                        'Profit Margin': value_list[4],
                                        'Operating Margin': value_list[5],
                                        'Return on Assets': value_list[6],
                                        'Return on Equity': value_list[7],
                                        'Revenue Per Share': value_list[8],
                                        'Market Cap': value_list[9],
                                        'Enterprise Value': value_list[10],
                                        'Forward P/E': value_list[11],
                                        'PEG Ratio': value_list[12],
                                        'Enterprise Value/Revenue': value_list[13],
                                        'Enterprise Value/EBITDA': value_list[14],
                                        'Revenue': value_list[15],
                                        'Gross Profit': value_list[16],
                                        'EBITDA': value_list[17],
                                        'Net Income Avl to Common ': value_list[18],
                                        'Diluted EPS': value_list[19],
                                        'Earnings Growth': value_list[20],
                                        'Revenue Growth': value_list[21],
                                        'Total Cash': value_list[22],
                                        'Total Cash Per Share': value_list[23],
                                        'Total Debt': value_list[24],
                                        'Current Ratio': value_list[25],
                                        'Book Value Per Share': value_list[26],
                                        'Cash Flow': value_list[27],
                                        'Beta': value_list[28],
                                        'Held by Insiders': value_list[29],
                                        'Held by Institutions': value_list[30],
                                        'Shares Short (as of': value_list[31],
                                        'Short Ratio': value_list[32],
                                        'Short % of Float': value_list[33],
                                        'Shares Short (prior ': value_list[34],
                                        'Status': status}, ignore_index=True)
                except Exception as e:
                    pass
    # for eachTicker in tickerList:
    #     try:
    #         plotDf = df[(df['Ticker'] == eachTicker)]
    #         plotDf = plotDf.set_index(['Date'])
    #
    #         if plotDf['Status'][-1] == "underperform":
    #             colour = 'r'
    #         else:
    #             colour = 'g'
    #
    #         plotDf['Difference'].plot(label=eachTicker, color = colour)
    #
    #         plt.legend()
    #     except:
    #         pass
    # plt.show()
    #
    df.to_csv("key_stats.csv")
Key_Stats()




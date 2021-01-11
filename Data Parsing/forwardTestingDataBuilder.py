import pandas as pd
from pandas.plotting import register_matplotlib_converters


import numpy as np
import os
import time
from datetime import datetime
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
import re

# path = "/intraQuarter"
# sp500Df = pd.read_csv("C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/YAHOO-INDEX_GSPC.csv")
# stockDf = pd.read_csv("C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/stock_prices.csv")
# change according to where intraQuarter folder is stored

def Forward(gather=["Total Debt/Equity",
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
    # statsPath = path + '/_KeyStats'
    # stockList = [x[0] for x in os.walk(statsPath)] # gather all stock names from folder
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
                               'Shares Short (prior month)',
                               ##############
                               'Status'])

    fileList = os.listdir("../Data files/forward")

    for eachFile in fileList[:]:
        ticker = eachFile.split(".html")[0]
        fullFilePath = "Data files/forward/"+eachFile
        source = open(fullFilePath, "r").read()

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
            print("Last processed file: ", str(ticker) + ".html")

            if value_list.count("N/A") > 15 | value_list.count(np.nan) > 15 | value_list.isnull().count() > 15 | value_list.count(None) > 15 | value_list != None | value_list != []:
                pass
            else:

                df = df.append({'Date': "N/A",
                                'Unix': "N/A",
                                'Ticker': ticker,

                                'Price': "N/A",
                                'stock_p_change': "N/A",
                                'SP500': "N/A",
                                'sp500_p_change': "N/A",
                                'Difference': "N/A",
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
                                'Shares Short (prior month)': value_list[34],
                                'Status': "N/A"}, ignore_index=True)
        except Exception as e:
            pass


    df.to_csv("forward_sample_WITH_NA.csv")
Forward()




import pandas as pd
import os
import time
from datetime import datetime

path = "C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/intraQuarter"
# change according to where intraQuarter folder is stored

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statsPath = path + '/_KeyStats'
    stockList = [x[0] for x in os.walk(statsPath)] # gather all stock names from folder
    #print(stockList)
    df = pd.DataFrame(columns = ['Date', 'Unix', 'Ticker', 'DE Ratio', 'Price', 'SP500'])

    sp500df = pd.read_csv("YAHOO-INDEX_GSPC.csv")

    for eachDir in stockList[1:25]:
        eachFile = os.listdir(eachDir)
        ticker = eachDir.split("\\")[1]
        if len(eachFile) > 0:
            for file in eachFile:
                dateStamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unixTime = time.mktime(dateStamp.timetuple())
                fullPath = eachDir + '/' + file
                source = open(fullPath, 'r').read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])

                    try:
                        sp500Date = datetime.fromtimestamp(unixTime).strftime("%Y-%m-%d")
                        row = sp500df[(sp500df["Date"] == sp500Date)]
                        sp500Value = float(row["Adj Close"])
                    except:
                        sp500Date = datetime.fromtimestamp(unixTime-259200).strftime("%Y-%m-%d")
                        row = sp500df[(sp500df["Date"] == sp500Date)]
                        sp500Value = float(row["Adj Close"])

                    stockPrice = float(source.split("</small><big><b>")[1].split('</b></big>')[0])
                    #print("stock_price:", stockPrice, "ticker:", ticker)


                    df = df.append({'Date':dateStamp,
                                    'Unix':unixTime,
                                    'Ticker':ticker,
                                    'DE Ratio':value,
                                    'Price':stockPrice,
                                    'SP500':sp500Value}, ignore_index=True)
                except Exception as e:
                    pass
    save = gather.replace(' ', '').replace(')', '').replace('(', '').replace('/','')+'.csv'
    print(save)
    df.to_csv(save)
Key_Stats()




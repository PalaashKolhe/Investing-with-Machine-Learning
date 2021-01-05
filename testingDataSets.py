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

    for eachDir in stockList[1:]:
        eachFile = os.listdir(eachDir)
        if len(eachFile) > 0:
            for file in eachFile:
                dateStamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unixTime = time.mktime(dateStamp.timetuple())
                print(dateStamp, unixTime)
                time.sleep(15)

Key_Stats()




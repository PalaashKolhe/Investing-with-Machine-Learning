import urllib.request
import os
import time

path = "C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/intraQuarter"

def CheckYahoo():
    statspath = path+"/_KeyStats"
    stockList = [x[0] for x in os.walk(statspath)]

    for e in stockList[1:]:
        try:
            e = e.replace("C:/Users/kolhe/PycharmProjects/Investing-with-Machine-Learning/intraQuarter/_KeyStats\\", "")
            link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
            resp = urllib.request.urlopen(link).read()

            save = "Data files/forward/"+str(e)+".html"
            store = open(save, "w")
            store.write(str(resp))
            store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)
CheckYahoo()


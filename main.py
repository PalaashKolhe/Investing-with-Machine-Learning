#from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing, utils
import pandas as pd
from matplotlib import style
import statistics
style.use("ggplot")

FEATURES =  ['DE Ratio',
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
             'Shares Short (prior month)']

def BuildDataSet():
    dataDf = pd.read_csv("Data files/key_stats_acc_perf_WITH_NA.csv")

    # shuffles our data
    dataDf = utils.shuffle(dataDf)

    # replaces the n/a in dataframe
    dataDf = dataDf.fillna(0)


    X = np.array(dataDf[FEATURES].values.tolist()) # consider features only and convert to python list
    y = (dataDf["Status"]
         .replace("underperform", 0)
         .replace("outperform", 1)
         .values.tolist())

    X = preprocessing.scale(X)
    Z = np.array(dataDf[["stock_p_change","sp500_p_change"]])

    return X,y,Z

def Analysis():
    testSize = 1

    investAmount = 10000
    totalInvests = 0
    ifMarket = 0
    ifStrat = 0

    X,y,Z = BuildDataSet()
    print(len(X))

    clf = svm.SVC(kernel="linear", C=1.0) # decide what classifier is
    clf.fit(X[:-testSize],y[:-testSize]) # train classifier

    for x in range(1, testSize+1):
        if clf.predict([X[-x]])[0] == 1:
            investReturn = investAmount + (investAmount * (Z[-x][0]/100))
            marketReturn = investAmount + (investAmount * (Z[-x][1]/ 100))

            totalInvests += 1
            ifMarket += marketReturn
            ifStrat += investReturn

    # predict our training exmaples
    correctCount = np.sum(clf.predict(X[-testSize:]) == y[-testSize:])
    # print("Accuracy:", (correctCount / testSize) * 100)
    # print("Total Trades:", totalInvests)
    # print("Ending with Strategy:", ifStrat)
    # print("Ending with Market:", ifMarket)

    compared = ((ifStrat - ifMarket) / ifMarket) * 100
    doNothing = totalInvests * investAmount
    avgMarket = ((ifMarket - doNothing) / doNothing) * 100
    avgStrat = ((ifStrat - doNothing) / doNothing) * 100

    # print("Comapred to market, we earn", str(compared) + "% more")
    # print("Average investment return:", str(avgStrat)+"%")
    # print("Average market return:", str(avgMarket)+"%")

    dataDf = pd.read_csv("Data files/forward_sample_WITH_NA.csv")

    dataDf = dataDf.fillna(0)
    X = np.array(dataDf[FEATURES].values.tolist())  # consider features only and convert to python list
    X = preprocessing.scale(dataDf[FEATURES])
    Z = dataDf["Ticker"].values.tolist()
    investList = []
    for i in range(len(X)):
        p = clf.predict([X[i]])[0]
        if p == 1:
            investList.append(Z[i])

    print(len(investList))
    print(investList)

Analysis()


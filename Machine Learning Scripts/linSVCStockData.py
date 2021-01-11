#from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
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
             'Shares Short (prior ']

def BuildDataSet():
    dataDf = pd.read_csv("../Data files/key_stats.csv")

    #dataDf = dataDf[:100]
    dataDf = dataDf.reindex(np.random.permutation(dataDf.index))

    X = np.array(dataDf[FEATURES].values) #.tolist()) # consider features only and convert to python list
    y = (dataDf["Status"].replace("underperform", 0).replace("outperform", 1).values.tolist())

    X = preprocessing.scale(X)

    return X,y

def Analysis():
    testSize = 1000
    X,y = BuildDataSet()
    print(len(X))


    clf = svm.SVC(kernel="linear", C=1.0) # decide what classifier is
    clf.fit(X[:-testSize],y[:-testSize]) # train classifier

    correctCount = 0

    correctCount = np.sum(clf.predict(X[-testSize:]) == y[-testSize:])

    print("Accuracy:", (correctCount/testSize) * 100)

    # graph code
    # w = clf.coef_[0]
    # a = -w[0] / w[1]
    #
    # xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
    # yy = a * xx - clf.intercept_[0] / w[1]
    #
    # h0 = plt.plot(xx,yy, "k-", label="non weighted")
    #
    # plt.scatter(X[:, 0], X[:, 1], c=y)
    # plt.ylabel("Trailing P/E")
    # plt.xlabel("DE Ratio")
    # plt.legend()
    #plt.show()

# def Randomizing():
#     df = pd.DataFrame({"D1":range(5), "D2":range(5)})
#     print(df)
#     df2 = df.reindex(np.random.permutation(df.index))
#     print(df2)


Analysis()


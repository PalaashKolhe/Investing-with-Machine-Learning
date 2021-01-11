# Investing with Machine Learning
Using machine learning to discern characteristics of companies that perform well over a long term period. 

The machine learning model has been trained from free stock data provided from Quandl. With this data spanning all the way back to 2000, it trains off of 36 different factors to be able to label a stock as an underperformer or an outperformer. 

## The Machine Learning Model
The Scikit-learn library is implemented in this project. Particularly the supervised machine learning functions. 

## The Dataset
The training dataset is pulled from Quandl. Various scripts have been run on this raw dataset to label them and produce more refined datasets that can be used for SVM.

## How it works
The individual stocks are compared to the S&P 500 market's price. If the individual stock is worth a certain chosen percent more than the S&P 500 market, then it is labelled as an outperformer. This chosen percent can be manipulated in the main.py file.  

The machine learning algorithm is run multiple times to filter for stocks that might have luckily passed the algorithm the first time. This way, one potential error has been reduced. 

Run the main.py file to see which stocks are worth buying!



NOTE: This is a purely educational project and should not be used to make any real financial decisions. 

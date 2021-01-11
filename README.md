# Investing with Machine Learning
Using __machine learning__ to discern characteristics of companies that perform well over a long term period. 

The machine learning model has been trained from free stock data provided from Quandl. With this data spanning all the way back to 2000, it trains off of __36 different factors__ to be able to label a stock as an underperformer or an outperformer. 

## The Machine Learning Model
The __Scikit-learn library__ is implemented in this project. Particularly the supervised machine learning functions. 

## The Dataset
The training dataset is pulled from Quandl. Various scripts have been run on this raw dataset to label them and produce more refined datasets that can be used for SVM.

## How it works
The individual stocks are compared to the S&P 500 market's price. If the individual stock is worth a certain chosen percent more than the S&P 500 market, then it is labelled as an outperformer. This chosen percent can be manipulated in the ```main.py``` file.  

The machine learning algorithm is run multiple times to filter for stocks that might have luckily passed the algorithm the first time. This way, one potential error has been reduced. 

Run the main.py file to see which stocks are worth buying!



__NOTE__: This is a purely educational project and __should not be used to make any real financial decisions.__ 

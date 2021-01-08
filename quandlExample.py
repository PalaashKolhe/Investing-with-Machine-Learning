import pandas as pd
import os
import quandl
import time

authTok = open('auth.txt', 'r').read() # auth token saved locally in txt file
quandl.ApiConfig.api_key = authTok
data = quandl.get("WIKI/KO", trim_start="2000-12-12", trim_end="2014-12-30")
print(data["Adj. Close"])
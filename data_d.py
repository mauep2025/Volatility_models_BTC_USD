# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:02:30 2021

@author: Mauricio
"""
# Download the data from Yahoo Finance
import time
import datetime
import pandas as pd
ticker = 'BTC-USD'
time1 = int(time.mktime(datetime.datetime(2015, 1, 1).timetuple()))
time2 = int(time.mktime(datetime.datetime(2020, 12, 31).timetuple()))
interval = '1d' 

btcusd_s = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={time1}&period2={time2}&interval={interval}&events=history&includeAdjustedClose=true'

#Storing the data in SQL

# Storing the data in excel
sd = pd.read_csv(btcusd_s)
#sd.dropna(subset = ["Close"], inplace=True)
print(sd)
sd.to_csv('BTC_USD_day.csv')




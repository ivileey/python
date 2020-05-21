# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:51:02 2019

@author: Administrator
"""
import requests,re
import json
from datetime import date
import pandas as pd
import time
import matplotlib.pyplot as plt
def retrieve_quotes_historical(stock_code):
    quotes=[]
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r=requests.get(url)
    except ConnectionError as err:
        print(err)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]
quotes = retrieve_quotes_historical('KO')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes,index = list1)
quotesdf = quotesdf_ori.drop(['date'],axis=1)#axis = 0 夸行 axis=1跨列
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],'%Y-%m-%d')
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp
closeMeansKO = tempdf.groupby('month').close.mean()    
print(closeMeansKO)
x = closeMeansKO.index
y = closeMeansKO.values
plt.plot(x, y)
plt.savefig('1.jpg')
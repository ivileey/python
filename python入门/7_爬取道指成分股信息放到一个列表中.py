# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:01:59 2019

@author: Administrator
"""

import requestes,re
def request_dji():
    r=requestes.get('https://money.cnn.com/data/dow30/')
    pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list = re.findall(pattern,r.text)
    return dji_list
dji_list=request_dji()
print(dji_list)
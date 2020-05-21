# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:57:06 2019

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re
s=0
r = requests.get('https://book.douban.com/subject/30283996/comments/')
soup = BeautifulSoup(r.text,'lxml')
pattern = soup.find_all('span','short')
for temp in pattern:
    print(temp.string)
regularStar = re.compile('span class="user-stars allstar(.*?) rating"')
Star = re.findall(regularStar,r.text)
for temp in Star:
    s+=int(temp)
print(s)
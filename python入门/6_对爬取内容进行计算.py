# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:44:35 2019

@author: Administrator
"""
import requests,re,time
from bs4 import BeautifulSoup


i=0
count=0
count_del = 0
lst_star=[]
s=0
while(count<50):
    try:    
        r=requests.get('https://book.douban.com/subject/26708119/comments/hot?p='+str(i+1))
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text,'lxml')
    comment = soup.find_all('span','short')
    pattern = re.compile('<span class="user-stars allstar(.*?)rating"')
    p = re.findall(pattern,r.text)
    for item in comment:
        count+=1
        if count>50:
            count_del+=1
        else:
            print(count,item.string)
    for star in p:
        lst_star.append(star)
    time.sleep(2)
    i+=1
    for star in lst_star[:-count_del]:
        s+=int(star)
if count>=50:
    print(s/len(lst_star[:-count_del]))
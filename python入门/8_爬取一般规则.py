# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:15:15 2019

@author: Administrator
"""
import requests,re

def crawler(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    pattern = re.compile('href="/en/vnl/2018/women/teams/.*?">\
(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+\
<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
    result=re.findall(pattern,r.text)
    return result

if __name__=="__main__":
    url='http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
    result=crawler(url)
    print(result)
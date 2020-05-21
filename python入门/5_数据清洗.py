# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:34:50 2019

@author: Administrator
"""

def clean_list(list):
    cleaned_list=[]
    for item in list:
        for c in item:
            if not c.isalpha():
                item = item.replace(c,'')
        cleaned_list.append(item)
    return cleaned_list
    
if __name__=="__main__":
    coffee_list=['32Latte','Americano30','/34Cappuccino','Mocha35']
    cleaned_list = clean_list(coffee_list)
    for k,v in zip(range(1,len(cleaned_list)+1),cleaned_list):
        print(k,v)
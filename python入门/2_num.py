# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:24:16 2019

@author: Administrator
"""

#输入一个整数将这个整数分解为最小质数相乘
n = int(input("Enter a number:"))
print(n,'=',end='')
i=2
while n!=1:
    while n%i==0:
        n=n/i
        if n==1:
            print(i)
        else:
            print("{:d} * ".format(i),end='')
    i+=1
        
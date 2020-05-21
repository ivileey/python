# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:05:07 2019

@author: Administrator
"""
def read_line(lines):
    lines.insert(0,"Blowing in the wind\n")
    lines.insert(1,"Bob Bylan\n")
    lines.append("1962 by Warner Bros.inc.")
    return ''.join(lines)
    
with open('Blowing in the wind.txt','r+') as f:
    lines = f.readlines();
    string =read_line(lines);
    print(string)
    f.seek(0)
    f.write(string)
    f.close()
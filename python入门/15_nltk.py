# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:28:07 2019

@author: Administrator
"""

from nltk.corpus import PlaintextCorpusReader
coprus_root = r'd:\data'
books= PlaintextCorpusReader(coprus_root,'*')
print(books.fileids())
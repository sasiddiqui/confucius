#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:18:17 2017

@author: soren
"""
#%%
import urllib.request

url = "http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do"
response = urllib.request.urlopen(url)
print('RESPONSE:', response)
print('URL     :', response.geturl())

headers = response.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)

data = response.read()
print('LENGTH  :', len(data))
print('DATA    :')
print('---------')
print(data)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:20:10 2017

@author: soren
"""
#%%
#filename = 'Posts.xml.retrieve.json'
filename = 'Posts.xml.ranker.csv'
with open(filename, "r") as file:
    lines = file.readlines()
with open('mod.'+ filename, 'w') as file:
    for line in lines:
        l = line.replace('\\"', '<bs-dic>').replace('""','<dic>')
        file.write(l)
    
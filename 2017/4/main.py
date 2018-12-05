#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:11:50 2017

@author: james
"""

from collections import Counter

file = open("input.txt", 'r')

total = 0
failed = 0

for i in file.read().split('\n'):
    if i=='':
        continue    
    total += 1
    split_line = i.split(' ')
    count = Counter( split_line )
    list_of_values = list( count.values() )
    for i in list_of_values:
        if i>1:
            failed += 1
            break

print("Number of failed: %d" % failed)
print("Number of passed: %d" % (total-failed) )
print("Total Number: %d" % total)
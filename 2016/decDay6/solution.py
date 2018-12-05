#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:06:12 2016

@author: james
"""

import collections

file = open('input.txt')

l=[x for x in file]
ans=""

'''
    Part 1 find the most common in repetition code   
'''
'''
for i in range(len(l[0])-1):
    word=""
    for j in range(len(l)):
        word+=l[j][i]
    ans+=collections.Counter(word).most_common(1)[0][0]

print(ans)    
'''

for i in range(len(l[0])-1):
    word=""
    for j in range(len(l)):
        word+=l[j][i]
    result= collections.Counter(word).most_common(len(l))
    ans+=result[len(result)-1][0]

print(ans)  
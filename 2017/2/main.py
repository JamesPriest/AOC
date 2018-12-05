#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:44:23 2017

@author: james
"""


file = open("input.txt", 'r')

text_input = file.read().split('\n')

text_input = [ i.split('\t') for i in text_input ]

text_input = text_input[:-1]

sum_total = 0

#for i in range(len(text_input)):
#    int_input = [ int(j) for j in text_input[i] ]
#    print("*************")
#    print(min(int_input))
#    print(max(int_input))
#    print(max(int_input) - min(int_input))
#    output = max(int_input) - min(int_input)
#    sum_total = sum_total + output

for i in range(len(text_input)):
    int_input = [ int(j) for j in text_input[i] ]
    print("*************")
    for j in int_input:
        for i in int_input:
            if( j%i == 0 and j/i != 1):
                print("j, i is %d, %d" % (j, i) )
                print('if hit')
                sum_total += j/i    

print(sum_total)
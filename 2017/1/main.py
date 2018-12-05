#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:03:24 2017

@author: james
"""

file  = open( "input.txt", "r" )

test = file.read()[:-1]

#test='12131415'

size = len(test)

skip = len(test)//2

output = 0

for i in range(len(test)):
    if( test[ (i)%size ] == test[ (i+skip)%size ]):
        print("*************")
        print( test[(i+skip)%size] )
        print(output)
        print("Hit")
        output += int( test[i%size] )

print("Final output is: %d" % output)
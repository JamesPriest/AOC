#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:41:29 2016

@author: james
"""

file =open('input.txt')
matrix= [['.' for j in range(50)] for i in range(6)]
#print(matrix)
x='test'
while( x != ""):
    x = file.readline()
    y = x.split(' ')
#    print(y)
    if(y[0] == 'rect'):
        y[1] = y[1].strip('\n')
        size=y[1].split('x')
        size = [int(j) for j in size]
        for i in range(size[0]):
            for j in range(size[1]):
                matrix[j][i] = '#'
#        print(matrix)
    elif(y[0] == 'rotate'):
        y = [j.strip('\n') for j in y]
        if(y[1] == 'column'):
            column=int(y[2][2:])
            dist=int(y[4])
            copy=[matrix[i][column] for i in range(len(matrix))]
            # Todo: Copy column into a hashtable, then reset column using values from hash table
            #print(copy)
            for i in range(len(matrix)):
                matrix[i][column]=copy[(i-dist)%len(matrix)]
        elif(y[1] == 'row'):
            row=int(y[2][2])
            dist=int(y[4])
            copy=[i for i in matrix[row]]
            #print(copy)
            for i in range(len(matrix[row])):
                matrix[row][i]=copy[(i-dist)%len(matrix[row])]

count=0
for j in range(len(matrix)):
    word=''
    for i in matrix[j]:
        if(i=='#'):
            count+=1
        word+=i
    print(word)
print(count)
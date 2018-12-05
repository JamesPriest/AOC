#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:15:13 2016

@author: james
"""

file=open('input.txt')

sides=[]

for line in file:
    fix=line[2:].split('  ')
    if('' in fix):
        fix.remove('')
    fix[2]=fix[2][:-1]
    sides+=fix
    
#print(sides)
sidesInt=[int(x) for x in sides]
#print(sidesInt)
possible=0

for i in range(int(len(sidesInt)/3)):
    j=3*i
    if((sidesInt[j]+sidesInt[j+1]>sidesInt[j+2]) and (sidesInt[j]+sidesInt[j+2]>sidesInt[j+1]) and (sidesInt[j+2]+sidesInt[j+1]>sidesInt[j])):
        possible+=1
        
print(possible)
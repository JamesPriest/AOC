#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:43:32 2017

@author: james
"""


def count_cycle_length( cycle ):
    index = cycle.index( max(cycle) )
    length = 0
    end = list(cycle)
    current = list(cycle)
    while True:
        if( current[index] == max(current) ):
            saved = current[index]
            current[index] = 0
            temp = index
            while( saved > 0 ):
                temp = (temp+1)%len(current)
                current[temp]+=1
                saved-=1
            length+=1
            index=0
            if current == end:
                break
        else:
            index = (index+1)%len(current)
    return length

with open('input.txt', 'r') as file:
    toDecode = file.read()
    

initial = [ int(i) for i in toDecode.strip('\n').split('\t') ] 

#initial = [0, 2, 7, 0]
history = []

history.append(list(initial))

current = initial

test = 0
index = 0

cycle = 0
    
while True:
    if( current[index] == max(current) ):
        saved = current[index]
        current[index] = 0
        temp = index
        while( saved > 0 ):
            temp = (temp+1)%len(current)
            current[temp]+=1
            saved-=1
        cycle+=1
        index=0
        if current in history:
            print('HIT')
            print("CYCLES ARE: %d" % cycle)
            print("CYCLE LENGTH IS: %d" % count_cycle_length(current) )
            break
        history.append(list(current))
    else:
        index = (index+1)%len(current)


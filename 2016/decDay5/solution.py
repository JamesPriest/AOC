#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:23:11 2016

@author: james
"""

import hashlib as hl

'''
Part 1 code solution
for hashing secret password
'''

'''
doorID='ugkcyxxp' #'abc'
largeNum=10**8
print(largeNum)
password=""
count=0
for i in range(largeNum):
    ht = hl.md5()
    doorCode=doorID+str(i)
    ht.update(doorCode.encode('utf-8'))
    result=ht.hexdigest()
    if(result[0:5]=='00000'):
        print(i)
        password+=str(result)[5]
        count+=1
    if(count==8):
        break

print(password)
'''

'''
Part 2
'''
doorID= 'ugkcyxxp' # 'abc'
largeNum=10**9
print(largeNum)
count=0
loc=0
password=['_']*8
for i in range(largeNum):
    #if(i%10**6==0):
    #    print('count is ' + str(count) + ' and i is ' + str(i))
    ht = hl.md5()
    doorCode=doorID+str(i)
    ht.update(doorCode.encode('utf-8'))
    result=ht.hexdigest()
    if(result[0:5]=='00000'):
        #print(i)
        #print("result is " + str(result))
        if(str(result)[5].isalpha()):
            continue
        else:
            loc=int(str(result)[5])
        #print(loc)
        if(loc>7):
            continue
        if(password[loc]=='_'):
            password[loc]=str(result)[6]
            count+=1
            print(''.join(password))
    if(count==8):
        break

print(''.join(password))
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:48:35 2020

@author: ADMIN
"""
#12.1.1
import random
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res
num = 1 
start = 50
end = 1000
print (Rand(start, end, num))  

#12.1.2
import random
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res
num = 10 
start = -1000
end = 1000
print (Rand(start, end, num))   

#12.1.3
import random
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.uniform(start, end))
    return res
num = 10 
start = -1000
end = 1000
print (Rand(start, end, num))        
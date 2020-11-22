# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:02:34 2020

@author: ADMIN
"""

import numpy as np
n= int(input("số phần tử của list="))
rd= np.random.random_sample(size = n)*4000000-3000000
print("list =",rd)
max = rd[1]
for x in rd :
     if x > max :
        max = x
print("giá trị lớn nhất của list =",max)
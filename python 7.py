# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:55:53 2020

@author: ADMIN
"""

import numpy as np
n = int(input("Số phần tử của list ="))
rd = np.random.random_sample(size = n)*5000000-4000000
print ("list =",rd)
min = rd[1]
for a in rd :
    if a < min:
        a = min
print ("Giá trị nhỏ nhất của list =",min)
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:56:43 2020

@author: ADMIN
"""

import numpy as np
n = int(input("Số các giá trị các phần tử ="))
rd = np.random.random_sample(size = n)*30000000-20000000
n = 1
print ("Giá trị các phần tử =",rd)
import math
for x in rd:
    print ("Giá trị các phần tử thứ ",n,"=",x)
    n=n+1
    if x > 0:
         print ("Logarith của các phần tử thứ",n,"=",math.log(x))
    else:
        print ("Không có logarith")
        
   


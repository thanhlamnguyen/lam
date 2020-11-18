# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:03:41 2020

@author: ADMIN
"""

a=[1,-3,22,55,-69,85,2]
n=1
import math
for x in a:
    print ("giá trị của các phần tử",n,'=',x)
    n=n+1
    if x>0 :
        print ('Logarith của các phần tử thứ',n,'=',math.log(x))
    else :
        print ('Không có Logarith')
        
        
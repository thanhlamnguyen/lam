# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:07:26 2020

@author: ADMIN
"""

list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for a in list2:
   #print(a)
    for x in a:
        print (x)
        for index, j in enumerate(x):
            print (j,":", x[j])
           
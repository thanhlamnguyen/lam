# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 22:25:05 2020

@author: ADMIN
"""
#1.Tạo ngẫu nhiên số  phần tử của List  50 <= n <= 100
import numpy as np
n = int(input("nhap vao so phan tu cua list= "))
rd = np.random.random_sample(size=n)*200000-100000
print("list= ",rd)

#2. Tạo  ngẫu nhiên List gồm n phần tử với cấu trúc sau: [{'name': ' sinh ngẫu nhiên', 'age': 'sinh ngẫu nhiên'}] có tất cả n dictionary như trên trong List.
import random, string
n = random.randint(50,100)
x = list()
i=1
for i in range(n):
    l=random.randint(2,5)
    y = dict()
    g = random.choice(string.ascii_uppercase)
    p = g + ''.join(random.choice(string.ascii_lowercase) for _ in range(l - 1))
    y['name'] = p
    h = random.randint(1, 100)
    y['age'] =h
    x.append(y)
print(x)
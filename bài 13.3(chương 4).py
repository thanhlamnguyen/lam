

import random
import string


def text(): 
    c=''.join(random.sample(f,t))
    return c


dulieu = int(input('nhập giới hạn dữ liệu(MB)= '))
while (dulieu<1 or dulieu>1024):
	dulieu = int(input('nhập lại giới hạn dữ liệu (1->1024MB)= '))
t = 1000*1024 
a = dulieu*(2**20)//(t) 
b = dulieu*(2**20)%(t)
f = string.ascii_lowercase*48733
def text(): 
    c=''.join(random.sample(f,t))
    return c
print('số file có kích thước 1000KB là: ', a)
print('file cuối cùng có kích thước: ', b/1024,"KB")
for i in range(a): 
	file = open('oejb'+str(i+1)+'.txt' ,'x')
	file.write(text())
	file.close()
if b > 0: 
    file = open('pêns'+'.txt' ,'x')
    file.write(''.join(random.sample(f,b)))
file.close()
print('Kết thúc')

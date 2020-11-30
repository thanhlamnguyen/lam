# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:20:48 2020

@author: ADMIN
"""

# Numby
    # 1: Tạo ma trận
import numpy as np
x = [[1,2,3], [4,5,6]]
print ('a =',np.array(x))

    # 2: Tình tổng, tích hai ma trận
import numpy as np
x = [((1,2),(3,4)), ((4,5),(6,7))]
y = [((6,7),(8,9)), ((9,10),(11,12))]
a = np.array(x)
b = np.array(y)
print ('a+b =',a + b)
print ('a*b =',a.dot(b))

    # 3: Tính chuyển vị
import numpy as np
x = [[1,2,3], [4,5,6]]
y = np.transpose(x)
print ('ma trận của x',x)
print ('ma trận chuyển vị của x',y)

# Matplotlib
    # Column
import matplotlib.pyplot as plt
divisions = ["Dog","Cat","Mouse","Rabbit","Bird"]
divisions_average_marks = [80,70,30,20,25]
plt.bar(divisions, divisions_average_marks, color = 'green')
plt.title("Trung bình mỗi người nuôi thú cưng trong 1 năm")
plt.xlabel("Các thú cưng")
plt.ylabel("Tỉ lệ %")
plt.show()

    # Bar
import matplotlib.pyplot as plt
import numpy as np
divisions = ["Năm 2017", "Năm 2018", "Năm 2019", "Năm 2020"]
divisions_average_marks = [80,70,85,90]
boys_average_marks = [70,75,80,95]
index = np.arange(4)
width = 0.20
plt.bar(index, divisions_average_marks, width, color='red', label='Dog')
plt.bar(index+width, boys_average_marks, width, color='green', label='Cat')
plt.title("Bản so sánh độ yêu thích giữa Dog & Cat từ năm 2017-2020")
plt.xlabel("Các năm")
plt.ylabel("Tỉ lệ %")
plt.xticks(index+ width/2, divisions)
plt.legend(loc='best')
plt.show()

    # Line
import matplotlib.pyplot as plt
import numpy as np
plt.plot([2015,2017,2020],[10,20,30])
plt.title("Lượng mưa trung bình trong 1 ngày trong các năm từ 2015-2020")
plt.xlabel("Các năm")
plt.ylabel("Phần trăm")
plt.show()

    # Box plot
u = u"""index,location,price
    Apr 25,ASHEVILLE,15.0
    Apr 25,ASHEVILLE,45.0
    Apr 25,ASHEVILLE,50.0
    Apr 25,ASHEVILLE,120.0
    Apr 25,ASHEVILLE,300.0"""

import io
import pandas as pd
import matplotlib.pyplot as plt

data = io.StringIO(u)

df = pd.read_csv(data, sep=",", index_col=0)

plt.boxplot(df["price"])
plt.show()








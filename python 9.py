# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:35:24 2020

@author: ADMIN
"""

import os
import time
shutdown = True
while shutdown:
    shutdown = input("Do you want to Tắt nguồn? (nhập yes hoặc no) ")
    if shutdown =="yes" :
        os.system('shutdown -s')
        shutdow = False                 
    else:
        print("chờ 1 chút rồi được hỏi lại")
        time.sleep(30)
        shutdown = True
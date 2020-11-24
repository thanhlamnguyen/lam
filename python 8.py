# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:07:51 2020

@author: ADMIN
"""
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("luckylucy0912102915@gmail.com","thanhlam0914620225")
msg = "16 Typh on the mic"
for i in range(7):
    if i <= 7:
        server.sendmail("luckylucy0912102915@gmail.com","nguyenthanhlam06072002@gmail.com",msg)
        i+=1
server.quit()
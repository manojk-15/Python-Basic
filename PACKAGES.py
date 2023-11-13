# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:43:02 2023

@author: Manoj kumar
"""


#PACKAGES
import datetime
x=datetime.datetime.now()
print (x)

x=datetime.date.today()
print(x)

x=datetime.datetime(2010,1,1)
print(x)

import datetime
for i in range(2010,2024):
    x=datetime.date(i,1,31)
    y=data.strftime("A")
    print

data=datetime.datetime.now()
print(data.strftime("%a"))
print(data.strftime("%A"))
print(data.strftime("%w"))
print(data.strftime("%d")) #date
print(data.strftime("%b"))
print(data.strftime("%B"))
print(data.strftime("%m"))
print(data.strftime("%M"))
print(data.strftime("%y"))
print(data.strftime("%Y"))
print(data.strftime("%H")) #railwaytime
print(data.strftime("%I")) #12hrs timing
print(data.strftime("%p")) #am/pm
print(data.strftime("%S")) #seconds
print(data.strftime("%c"))
print(data.strftime("%C"))
print("EOD")
print("New line")







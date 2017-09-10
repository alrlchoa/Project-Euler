# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:15:45 2016

@author: Arnold Choa
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import matplotlib.animation as animation
import math
import time
import itertools as iter

start_time = time.time()

months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 2 # 1 Jan 1901 is a Tuesday
suns = 0

for i in range(1901,2001,1):
    if (i%400 == 0) or ((i%100 != 0) and (i%4 == 0)):
        months[1] = 29
    else:
        months[1] = 28

    for j in range(0,12,1):
        if ((days)%7) == 0:
            suns += 1
            print(i,j+1)
        days += months[j]

print(suns)

print("--------- %s seconds ---------" %(time.time() - start_time))
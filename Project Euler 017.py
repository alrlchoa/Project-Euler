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

result = 0

ones = [0,3,3,5,4,4,3,5,5,4,3]
teen = [0,6,6,8,8,7,7,9,8,8]
tens = [0,0,6,6,5,5,5,7,6,6]
hundred = 7
ands = 3

for i in range(1,100,1):
    if i <11:
        result += ones[i]
    elif i < 20:
        result += teen[i-10]
    else:
        result += (tens[int(i/10)] + ones[i%10])
result *= 10
result = result + 900*hundred + ands*891
temp = (sum(ones)-3)*100

result += temp + 11

print(result)

print("--------- %s seconds ---------" %(time.time() - start_time))
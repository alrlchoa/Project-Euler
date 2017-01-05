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

start_time = time.time()

sum = 0

def addTen(x,y):
    return (x % 10000000000) + (y % 10000000000)

for i in np.arange(1,1001,1):
    p = 1
    for j in np.arange(0,i,1):
        p = (p*i) % 10000000000
    sum = addTen(sum,p)
    
print(sum)

print("--------- %s seconds ---------" %(time.time() - start_time))
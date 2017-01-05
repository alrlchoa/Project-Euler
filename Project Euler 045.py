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

n = 286

while True:
    t = n*(n+1)/2
    
    if (((1 + math.sqrt(1+24*t))/6) %1 == 0) and (((1 + math.sqrt(1+8*t))/4) %1 == 0):
        print(t)
        break
    n += 1

print("--------- %s seconds ---------" %(time.time() - start_time))
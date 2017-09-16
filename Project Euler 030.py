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

suns = 0

for i in range(2, 354294, 1):
    temp = list(str(i))
    crit = 0
    
    for j in temp:
        crit += (int(j))**5
    
    if crit == i:
        suns += i

print (suns)
print("--------- %s seconds ---------" %(time.time() - start_time))
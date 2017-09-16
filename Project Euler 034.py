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

for i in range(3,10000000,1):        
    temp = 0
    crit = list(str(i))
    
    for j in crit:
        temp += math.factorial(int(j))
    
    if temp == i:
        suns += i
    
print(suns)

print("--------- %s seconds ---------" %(time.time() - start_time))
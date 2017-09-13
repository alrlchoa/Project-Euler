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

def isAbundant(x):
    crit = 1
    p = math.sqrt(x)
    
    if int(p) == p:
        crit += p
        p = int(p)
    else:
        p = int(p) +1
    
    for i in range(2,p,1):
        if x%i == 0:
            crit += i + (x/i)
        
    return crit > x

candidates = list(range(2,28123,1))
abundants = []
suns= [0] + ([1] * 28124)
result = 0

for i in range(2,28123,1):
    if isAbundant(i):
        abundants.extend([i])

for i in abundants:
    count = 0
    while (i + abundants[count] < 28123):
        suns[(i+abundants[count])] = 0
        count += 1

for i in range(0,28123,1):
    result += i * suns[i]

print(result)
print("--------- %s seconds ---------" %(time.time() - start_time))
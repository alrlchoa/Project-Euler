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

def findDiv(x):
    p = int(math.sqrt(x))
    divs = [1]
    
    for i in range(2,p,1):
        if(x%i ==0):
            divs.extend([int(i),int(x/i)])
    if x%p == 0:
        divs.extend([int(p)])
    return sum(divs)

for i in range(1,10000,1):
    x = findDiv(i)
    
    if (findDiv(x) == i) and (x != i):
        suns += i

print(suns)

print("--------- %s seconds ---------" %(time.time() - start_time))
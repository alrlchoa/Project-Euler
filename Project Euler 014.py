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

candidates = list(range(2,1000000,1))
longest = 0
seed = 0
lengths = [0,1]

for i in range (2,1000000,1):
    x=i
    count = 1
    
    while x >= i:
        if x%2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        count += 1
        
    lengths.extend([count + lengths[int(x)]])

print(lengths.index(max(lengths)))

print("--------- %s seconds ---------" %(time.time() - start_time))
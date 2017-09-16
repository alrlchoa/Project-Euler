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

suns = 1
current = 1

for i in range (3, 1002, 2):
    skips = i - 1
    
    for j in range(0,4,1):
        current += skips
        suns += current

print(suns)
print("--------- %s seconds ---------" %(time.time() - start_time))
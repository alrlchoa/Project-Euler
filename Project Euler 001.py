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

sum = 0

for i in range(0,1000,3):
    sum += i
    
for i in range(0,1000,5):
    sum += i

for i in range(0,1000,15):
    sum -= i

print(sum)

print("--------- %s seconds ---------" %(time.time() - start_time))
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

a = list('0')

for i in np.arange(1,1000000,1):
    a.extend(list(str(int(i))))
    if len(a) > 1000001:
        break

product = 1

for i in (1,10,100,1000,10000,100000,1000000):
    product *= int(a[i])
print("--------- %s seconds ---------" %(time.time() - start_time))
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

for c in range(333,1000,1):
    for b in range(1,1000-c,1):
        a = 1000 - b - c
        if (a**2 + b**2) == (c**2):
            print(a,b,c,a*b*c)
            break


print("--------- %s seconds ---------" %(time.time() - start_time))
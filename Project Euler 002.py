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

first = 1
second = 2
sum = 0

while second < 4000000:
    if second%2 == 0:
        sum += second
    temp = first + second
    first = second
    second = temp

print(sum)
            

print("--------- %s seconds ---------" %(time.time() - start_time))
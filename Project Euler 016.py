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

result = 0

for i in str(2**1000):
    result += int(i)
    
print(result)

print("--------- %s seconds ---------" %(time.time() - start_time))
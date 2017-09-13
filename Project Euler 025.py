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

count = 2

a = 1
b = 1

while len(list(str(b))) < 1000:
    count += 1
    a,b = b, b+a

print(count)
print("--------- %s seconds ---------" %(time.time() - start_time))
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

result = set()

for a in range(2,101,1):
    for b in range(2,101,1):
        result.add(a**b)

print(len(result))
print("--------- %s seconds ---------" %(time.time() - start_time))
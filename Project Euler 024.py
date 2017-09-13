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

candidates = list(range(0,10,1))
answer = ""
current = 1000000
    
i = 0
while len(candidates) > 0:
    p = ((i+1)*(math.factorial(len(candidates)-1)))
    if  p+1 > current:
        answer = answer + str(candidates[i])
        candidates.remove(candidates[i])
        current -= ( (p*i/(i+1)))
        i = 0
    else:
        i += 1


print(answer)
print("--------- %s seconds ---------" %(time.time() - start_time))
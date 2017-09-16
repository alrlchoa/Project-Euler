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

def hasNoRepeat(x):
    temp1 = list(str(x))
    temp2 = set(temp1)
    
    return len(temp1) == len(temp2)

def hasNoZero(x):
    temp = list(str(x))
    
    return not('0' in temp)

result = set()
crit = {1,2,3,4,5,6,7,8,9}

for i in range(1,10,1):
    for j in range(1000,10000,1):
        k = int(i*j)
        y = int(str(i)+str(j)+str(k))
        z = list(str(i)+str(j)+str(k))
        if (hasNoRepeat(y)) and (hasNoZero(y)):
            if len(z) == len(crit) == len(set(z)):
                result.add(k)

for i in range(10,100,1):
    if (hasNoRepeat(i)) and (hasNoZero(i)):
        for j in range(100,1000,1):
            k = int(i*j)
            y = int(str(i)+str(j)+str(k))
            z = list(str(i)+str(j)+str(k))
            if (hasNoRepeat(y)) and (hasNoZero(y)):
                if len(z) == len(crit) == len(set(z)):
                    result.add(k)

print(sum(result))

print("--------- %s seconds ---------" %(time.time() - start_time))
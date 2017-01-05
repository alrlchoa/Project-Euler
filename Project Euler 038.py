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

def isPandigital(x):
    answer = []
    if x % 5 != 0:
        values = [1,2,3,4,5,6,7,8,9]
        j = 1
        while len(values) > 0:
            a = j*x
            a = list(str(a))
            for k in a:
                if int(k) in values:
                    values.remove(int(k))
                    answer.extend(k)
                else:
                    return 0
                    break
            j = j + 1
        return int(''.join(answer))
    else:
        return 0

max = 0

for i in np.arange(1,9999,1):
    q = isPandigital(i)
    if q > max:
        max =q
    
print(max)
                

print("--------- %s seconds ---------" %(time.time() - start_time))
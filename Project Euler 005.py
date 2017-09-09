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
pro = 1
primes = [2,3,5,7,9,11,13,17,19]
factors = []

def primeFactor(x,p):
    result = []
    while x > 1:
        if x%p[0] == 0:
            result.extend([p[0]])
            x /= p[0]
        else:
            p = p[1:]
    return result
        

for i in range(20,0,-1):
    temp = primeFactor(i,primes)
    
    for j in temp:
        if j in factors:
            factors.remove(j)
    factors.extend(temp)

for i in factors:
    pro *= i
    
print(pro)

print("--------- %s seconds ---------" %(time.time() - start_time))
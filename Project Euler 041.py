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

primes = [2]

max = 0

def isPrime(x):
    p = np.sqrt(x)
    for i in np.arange(3,p, 2):
        if x % i == 0:
            return False
            break
    return True
            
def isPandigital(x):
    values = [1,2,3,4,5,6,7]
    
    q = x
    
    while q > 0:
        w = q % 10
        if w in values:
            values.remove(w)
            q = q // 10
        else:
            return False
    return True
        
    
for j in np.arange(7654321,1234567,-2):
    if isPandigital(j):
        if isPrime(j):
            print(j)
            break
print("--------- %s seconds ---------" %(time.time() - start_time))
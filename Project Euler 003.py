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

x = 600851475143
n = int(math.sqrt(x))

def primeGen(n=1000000):
    candidates = [2]
    candidates.extend(list(range(3,n,2)))
    p = math.sqrt(n)

    for i in candidates:
        sieve = set(range(i+i,n,i))
        candidates = list(set(candidates).difference(sieve))
        if i > p:
            candidates.sort()
            return np.array(candidates)    

primes = primeGen(n+1)

i = 0

while x > 2:
    i = primes[0]
    if x%i == 0:
        x /= i
        print(i,x)
    else:
        primes = primes[1:]
        
print(i)
            

print("--------- %s seconds ---------" %(time.time() - start_time))
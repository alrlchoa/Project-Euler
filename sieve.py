# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:48:47 2016

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

n = 6

def primeGen(n=1000000):
    candidates = [2]
    candidates.extend(list(range(3,n,2)))
    p = math.sqrt(n)

    for i in candidates:
        sieve = set(range(i+i,n,i))
        candidates = list(set(candidates).difference(sieve))
        if i > p:
            candidates.sort()
            return candidates

primes = primeGen(10**n)

print(primes)



print("--------- %s seconds ---------" %(time.time() - start_time))
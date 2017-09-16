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

def makeCircle(x):
    temp = [x]
    start = list(str(x))
    succ = start
    t = succ[0]
    succ = succ[1:]
    succ.extend(t)
    while succ != start:
        temp.extend([int(''.join(succ))])
        t = succ[0]
        succ = succ[1:]
        succ.extend(t)
    
    return temp

def hasNone(x):
    temp = list(str(x))
    crit = ['0','2','4','5','6','8']
    
    for i in crit:
        if i in temp:
            return False
    return True

primes = primeGen()

i = 5

while i < len(primes):
    check = primes[i]
    
    if hasNone(check):
        hop = makeCircle(check)
        if all(x in primes for x in hop):
            i += 1
        else:
            for x in hop:
                if x in primes:
                    primes.remove(x)
    else:
        primes.remove(check)
    
print (i)
print("--------- %s seconds ---------" %(time.time() - start_time))
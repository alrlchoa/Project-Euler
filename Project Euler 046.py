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
#import Set
import time

start_time = time.time()

odds = set(range(1,10000,2)) # chose 10000 as arbritrary upper bound

primes = [2]

def isPrime(x):
    p = np.sqrt(x)
    for i in primes:
        if x % i == 0:
            return False
        if i > p:
            return True
        
    
for j in np.arange(3,10000,2):
    if isPrime(j):
        primes.extend([j])

odds = odds - set(primes) - set([1])

stuff = []

for i in primes:
    for j in np.arange(1, 10000,1):
        stuff.extend([i + 2*(j**2)])

print("here")

answer = odds - set(stuff)

print(answer)

print("--------- %s seconds ---------" %(time.time() - start_time))
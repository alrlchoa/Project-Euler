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

def isPrime(x):
    p = math.sqrt(x)
    
    i = 2
    
    while i <= p:
        if x%i == 0:
            return False
        
        i += 1
        
    return True

def primeGen(n=1000):
    candidates = [2]
    candidates.extend(list(range(3,n,2)))
    p = math.sqrt(n)

    for i in candidates:
        sieve = set(range(i+i,n,i))
        candidates = list(set(candidates).difference(sieve))
        if i > p:
            candidates.sort()
            return candidates

b = primeGen()
a = list(range(-999,1000,2))
maxer = 0
pro = 0

for i in a:
    for j in b:
        n = 0
        product = i*j
        res = n**2 + i*n + j
        
        while (res > 0) and isPrime(res):
            if maxer < n:
                maxer, pro, x, y = n, product, i, j
                
            n += 1
            res = n**2 + i*n + j

print(pro)
print("--------- %s seconds ---------" %(time.time() - start_time))
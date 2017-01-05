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

primes = primeGen(10**n)

index = np.where((np.array(primes)) > (10**(n-1)))[0][0]

primes = primes[int(index):]

print(primes)

def makeIndexes(x): # number of digits
    indexes = []
    indexPlaces = list(range(0,x,1))
    for i in range(1,7,1):
        a = list(iter.combinations(indexPlaces,i))[:]
        for k in a:
            indexes.append(list(k))
    return indexes
    

def makePermutes(n,x):
    indexes = []    
    slots = n-x
    num = ["0","1","2","3","4","5","6","7","8","9"]
    
    a = list(iter.combinations(num,slots))[:]
    for k in a:
            indexes.append(list(k))
    return indexes

def main():
    
    return 0
            

print("--------- %s seconds ---------" %(time.time() - start_time))
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

primes = [2]

def isPrime(x):
    p = np.sqrt(x)
    for i in primes:
        if x % i == 0:
            return False
        if i > p:
            return True

for j in np.arange(3,1000000,2):
    if isPrime(j):
        primes.extend([j])

max = 0
maxCount = 1

print ("Here")
for i in range(0,len(primes)//300,1):
    temp = primes[i]
    tempMax = 0
    tempCount = 0
    for k in range(1,maxCount,1):
        temp += primes[k+i]
    for j in range(i+maxCount,len(primes)//100,1):
        temp += primes[j]
        if temp in primes:
            tempCount = j-i
            tempMax = temp
    if tempCount > maxCount:
        max, maxCount = tempMax, tempCount
        print(max,maxCount,primes[i])
    
print(max)
    
    
        
        

print("--------- %s seconds ---------" %(time.time() - start_time))
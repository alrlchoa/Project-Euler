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

def isPrime(x):
    p = np.sqrt(x)
    for i in primes:
        if x % i == 0:
            return False
        if i > p:
            return True
        
    
for j in np.arange(3,1000000,2):
    if isPrime(j):
        primes = np.append(primes,j)
        

def isLeftTruncatable(x):
    global primes
    
    while x > 0:
        if x in primes:
            x = int(x/10)
        else:
            return False
            break
    return True

def isRightTruncatable(x):
    global primes 
    x = str(x)
    while len(x) > 1:
        x = int(x)
        if x in primes:
            x = list(str(x))
            x = ''.join(x[1:])
        else:
            return False
            break
    return int(x) in primes

answers = []

onePrimes = [2,3,5,7]

k = 11

while len(answers) < 11:
    if ((k % 10) in onePrimes) and (int(str(list(str(k))[0])) in onePrimes):
        if isLeftTruncatable(k) and isRightTruncatable(k):
            print(k)
            answers.append(k)
    k = k + 2
            
print(np.sum(np.array(answers)))

print("--------- %s seconds ---------" %(time.time() - start_time))
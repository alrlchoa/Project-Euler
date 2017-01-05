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

def helpMe(x,s):
    x = list(str(int(x)))
    for i in s:
        if i in x:
            x.remove(i)
        else:
            return False
    return True

def filter(s, criteria):
    answers = []
    for q in s:
        if helpMe(q,criteria):
            answers.extend([q])
    if len(answers) > 2:
        for i in range(0,len(answers),1):
            for j in range(i+1, len(answers),1):
                for k in range(j+1,len(answers),1):
                    if answers[j]-answers[i] == answers[k] - answers[j]:
                        print(answers[i],answers[j],answers[k])

runs = ["1","2","3","4","5","6","7","8","9"]

for i  in runs:
    a = runs[(int(i)-1):]
    for j in a:
        b = runs[(int(j)-1):]
        for k in b:
            c = runs[(int(k)-1):]
            for l in c:
                d = runs[(int(l)-1):]
                filter(primes,[i,j,k,l])
    
    
        
        

print("--------- %s seconds ---------" %(time.time() - start_time))
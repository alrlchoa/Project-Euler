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

pentagonals = []

def isItSpecial(a,b):
    c = a+b
    d = b-a
    
    addPenta = (1 + math.sqrt(1 + 24*c))/6
    difPenta = (1 + math.sqrt(1 + 24*d))/6
    
    if (addPenta % 1 == 0) and (difPenta % 1 == 0):
        print(a,b,c,addPenta,d,difPenta)
        return True
    
    return False

def pentaGen(n = 3001):
    global pentagonals
    for i in np.arange(1,n,1):
        temp = (i*(3*i - 1))/2
        pentagonals.extend([temp])

pentaGen(5001)

min = 300000000

for i in np.arange(0,4999,1):
    for j in np.arange(i+1,5000,1):
        if isItSpecial(pentagonals[i],pentagonals[j]):
            print(pentagonals[j] - pentagonals[i])

print("--------- %s seconds ---------" %(time.time() - start_time))
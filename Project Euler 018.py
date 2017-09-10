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

filename = "p018.txt"
f = open(filename,'r')
prob=[]

for line in f:
    prob.append(line.strip().split(' '))

prob.reverse()

while len(prob) > 1:
    x = prob[0]
    y = prob[1]
    
    for i in range(0,len(x)-1,1):
        y[i] = int(y[i]) + max(int(x[i]),int(x[i+1]))

    prob = prob[1:]
    
print(prob[0][0])
print("--------- %s seconds ---------" %(time.time() - start_time))
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

filename = "p011.txt"
f = open(filename, 'r')
prob = []
big = 0

def horizon(x):
    large = 0
    for i in range(0,len(x),1):
        for j in range(0, len(x[0])-4,1):
            test = 1
            for k in range(0,4,1):
                test *= int(x[i][j+k])
                large = max(large,test)
    return large

def vertical(x):
    large = 0
    for i in range(0,len(x)-4,1):
        for j in range(0, len(x[0]),1):
            test = 1
            for k in range(0,4,1):
                test *= int(x[i+k][j])
                large = max(large,test)
    return large

def rightCross(x):
    large = 0
    for i in range(0,len(x)-4,1):
        for j in range(0, len(x[0])-4,1):
            test = 1
            for k in range(0,4,1):
                test *= int(x[i+k][j+k])
                large = max(large,test)
    return large

def leftCross(x):
    large = 0
    for i in range(0,len(x)-4,1):
        for j in range(len(x[0])-1,2,-1):
            test = 1
            for k in range(0,4,1):
                test *= int(x[i+k][j-k])
                large = max(large,test)
    return large

for line in f:
    prob.append(line.strip().split(' '))

print(max(vertical(prob),horizon(prob),leftCross(prob),rightCross(prob)))


print("--------- %s seconds ---------" %(time.time() - start_time))
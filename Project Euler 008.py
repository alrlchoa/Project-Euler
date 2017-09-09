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

filename = "p008.txt"
f = open(filename, 'r')
prob = ""

for line in f:
    prob += line.strip()

prob = list(prob)

big = 0

for i in range(0,len(prob)-12,1):
    pro = 1
    for j in range(0,13,1):
        pro *= int(prob[i+j])
    big = max(pro,big)

print(big)

print("--------- %s seconds ---------" %(time.time() - start_time))
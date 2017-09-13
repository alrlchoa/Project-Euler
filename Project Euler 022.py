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

filename = "p022.txt"
f = open(filename, 'r')
prob = []
chars = ['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
suns = 0

for line in f:
    prob.extend(line.strip().split(','))

prob = np.sort(np.array(prob))

for i in range(0,len(prob),1):
    temp = 0
    x = list(prob[i])
    for j in x:
        temp += chars.index(j)
    suns += (i+1)*temp
    
print(suns)

print("--------- %s seconds ---------" %(time.time() - start_time))
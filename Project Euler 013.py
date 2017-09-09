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

filename = "p013.txt"
f = open(filename, 'r')
prob = 0

for line in f:
    temp = list(line)
    temp = temp[:13]
    temp = ''.join(temp)
    temp = int(temp)
    prob += temp

prob = list(str(prob))
prob = prob[:10]
print(''.join(prob))

print("--------- %s seconds ---------" %(time.time() - start_time))
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

maxlen = 0
maxer = 0

for i in range(2,1000,1):

    rest = 1   
    remainders = []
    count = 1
    
    while not (rest in remainders):
        count += 1
        remainders.extend([rest])
        rest = (10*rest)%i
        
    if count > maxlen:
        maxer = i
        maxlen = count
    

print(maxer)

print("--------- %s seconds ---------" %(time.time() - start_time))
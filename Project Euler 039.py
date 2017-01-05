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

bin = np.zeros((1001,))

def isPythagoreanTriple(a,b,c):
    
    return a**2 + b**2 == c**2
                
for c in np.arange(3,999,1):
    q = min(c,999-c)
    for b in np.arange(1,q,1):
        r = min(b,999-c-b)
        for a in np.arange(1,r,1):
            if isPythagoreanTriple(a,b,c):
                bin[int(a+b+c)] +=1

print (np.where(bin == max(bin)))


print("--------- %s seconds ---------" %(time.time() - start_time))
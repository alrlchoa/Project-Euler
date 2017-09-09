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

def isPalindrome(x):
    a = list(str(x))
    b = a[::]
    a.reverse()
    return (a==b)

large = 0

for i in range(100,1000,1):
    for j in range(i,1000,1):
        x = i*j
        if isPalindrome(x):
            large = max(large,x)

print(large)

print("--------- %s seconds ---------" %(time.time() - start_time))
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
    temp = list(str(x))
    temp2 = list(str(x))
    
    temp2.reverse()
    
    return temp2 == temp

suns = 0

for i in range(1,1000000,1):
    
    if isPalindrome(i):
        y = "{0:b}".format(i)
        if isPalindrome(y):
            suns += i

print(suns)

print("--------- %s seconds ---------" %(time.time() - start_time))
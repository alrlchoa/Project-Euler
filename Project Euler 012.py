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

def findDiv(x):
    p = int(math.sqrt(x))
    divs = 0
    
    for i in range(1,p,1):
        if(x%i ==0):
            divs +=2
    if x%p == 0:
        divs += 1
    
    return divs

def main():
    seed = 1
    count = 2
    while True:
        if findDiv(seed) > 500:
            print(seed)
            return
        seed += count
        count += 1

main()

print("--------- %s seconds ---------" %(time.time() - start_time))
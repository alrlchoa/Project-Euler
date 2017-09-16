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

coins = [200,100,50,20,10,5,2,1]

def trust(arr, goal):
    count = 0
    
    if goal == 0:
        return 1
    else:
        arr = [x for x in arr if x <= goal]
        while len(arr)>0:
            count += trust(arr,goal - arr[0])
            arr.remove(arr[0])
    
    return count

print (trust(coins,200))

print("--------- %s seconds ---------" %(time.time() - start_time))
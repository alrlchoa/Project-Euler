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
def relPrime(a, b):
    t = 0
    
    while(b != 0):
        t = a
        a = b
        b = t%b
    
    return a

def foundIt(num,den):
    x = list(str(num))
    y = list(str(den))
    
    for i in x:
        if i in y:
            x.remove(i)
            y.remove(i)
    
    if(len(x)==1):
        if (int(x[0])/int(y[0])) == (num/den):
            return True
        
    return False

temp = []

for i in range(10,100,1):
    if not(i%10 == 0):
        for j in range(10,i):
            if foundIt(j,i):
                temp.append([j,i])

num = 1
den = 1

for i in temp:
    num *= i[0]
    den *= i[1]
    
print(den / (relPrime(num,den)))

print("--------- %s seconds ---------" %(time.time() - start_time))
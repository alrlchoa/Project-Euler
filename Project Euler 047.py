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
#import Set
import time

start_time = time.time()

def primeFactorize(x):
    p = np.sqrt(x)
    answer = set([])
    i = 2
    while i <=p:
        if x % i ==0:
            answer = answer.union(set([i]))
            x = x/i
            p = np.sqrt(x)
        else:
            i += 1
    return answer.union(set([int(x)]))
    
answers = [0]

count = 1

j = 1

while True:
    if len(primeFactorize(j)) == 4:
        answers.extend([int(j)])
        if answers[-2] == answers[-1] -1:
            count += 1
            if count == 4:
                print(answers[-4])
                break
        else:
            count = 1
    j +=1

print("--------- %s seconds ---------" %(time.time() - start_time))
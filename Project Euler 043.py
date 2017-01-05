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

sum = 0

class Tree(object):
    def __init__(self):
        self.node = None
        self.children = []

build5 = ['0','1','2','3','4','6','7','8','9']
build0 = ['1','2','3','4','5','6','7','8','9']
buildTest = ['1','2','3']

def isItSpecial(a):
    primes = [0,1,2,3,5,7,11,13,17]
    for i in np.arange(1,9,1):
        test = int(''.join([a[i],a[i+1],a[i+2]]))
        if (test % primes[i]) != 0:
            return False
    
    return True
        
        

def buildTree(a,start): #a is list; start is root

    temp = Tree()
    temp.node = start    
    #print(a)
    
    if len(a) == 0:
        return temp
        
    else:
        for i in a:
            b = a[:]
            b.remove(i)
            #print(b)
            temp.children.append(buildTree(b,i))
    
    return temp

test = buildTree(build5,'')

def preorder(a, data = []):
    global sum
    
    if a.children == []:
        data.extend([a.node])
        data.insert(6,'5')
        if(isItSpecial(data)):
            sum += int(''.join(data))
    else:
        for i in a.children:
            b = data[:]
            b.extend([a.node])
            preorder(i,b)
        
preorder(test)

test = buildTree(build0,'')

def preorder(a, data = []):
    global sum
    
    if a.children == []:
        data.extend([a.node])
        data.insert(6,'0')
        if(isItSpecial(data)):
            sum += int(''.join(data))
    else:
        for i in a.children:
            b = data[:]
            b.extend([a.node])
            preorder(i,b)

preorder(test)

print(sum)
        

print("--------- %s seconds ---------" %(time.time() - start_time))
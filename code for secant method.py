# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:08:12 2022

@author: rifa tabassum mim
f(x) = e^x - x
"""
import math
import numpy as np
from xlwt import Workbook

def func(x):
    fx = math.exp(-x) - x
    return fx

x1 = float(input("Enter the first initial guess: "))
x2 = float(input('enter the second initial guess: '))
err = float(input('Enter the tolerable error: '))
ite = int(input('Enter the number of iteration: '))

fx1 = func(x1)
fx2 = func(x2)
 

x_1 = np.zeros([ite])
x_2 = np.zeros([ite])
f_x1 = np.zeros([ite])
f_x2 = np.zeros([ite])
x_3 = np.zeros([ite])
f_x3 = np.zeros([ite])
error = np.zeros([ite])
num_iter = np.zeros([ite])

x_1[0] = x1
x_2[0] = x2
f_x1[0] = fx1
f_x2[0] = fx2

for i in range(ite):
    f_x1[i] = func(x_1[i])
    f_x2[i] = func(x_2[i])
    x_3[i] = x_2[i] - ((f_x2[i]*(x_1[i]-x_2[i]))/(f_x1[i]-f_x2[i]))
    print(x_3[i])
    f_x3[i] = func(x_3[i])
    num_iter[i] = i+1
    
    if i>0:
        error[i] = ((x_3[i]-x_3[i-1])/x_3[i])*100
    if all ([i>0, abs(error[i])<err]):
        break 
    elif f_x3[i]==0:
        break
   
    if i==ite-1:
        break
        #replacement of values
    x_1[i+1] = x_2[i]
    x_2[i+1] = x_3[i]
    
print("the root is:",x_3[i])
    
    
    
    
    


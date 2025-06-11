# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 07:23:03 2021

@author: Kanan
"""
from math import * #google math functions in python
import docx
import modules 
#or import math, for more functions google "Python 3 math module"


#----------------------Functions---------------------------
def myfunc(a,b):
    #print(a,b)
    return a*b
    
output=myfunc(2, 3)
print(output)


#---------------------if statement-------------------------

def max_number1(num1, num2, num3):
    num_max=num1
    if num_max<=num2:
        num_max=num2
    if num_max<=num3:
        num_max=num3
    return num_max 

print(max_number1(3, 2, 1))  

def max_number2(num1, num2, num3):
    if num1>num2 and num1>=num3: #other comparision operator ==, != (not equal), 
        return num1
    elif num2>=num3:
        return num2
    else:
        return num3
               
            
print(max_number2(7, 3, 9))   

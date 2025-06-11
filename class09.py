# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:55:23 2021

@author: Kanan
"""


import numpy as np
import pandas as pa
import sklearn

# reference video https://www.youtube.com/watch?v=QUT1VHiLmmI


'''
a = np.array([1,2,3])
print(a)

b = np.array([[1,2,3,4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(b)

#Get dimension
print(a.ndim)
print(b.ndim) #counts rows


#Get shape
print(a.shape)
print(b.shape)

#Get data type
print(a.dtype)
print(b.dtype)
a1 = np.array([1.,2,3], dtype="int32") #int16 (two byte), int8 (one byte)
print(a1.dtype)

#Get total size
print(a.size*a.itemsize) #in byte, floats are 8 byte (by default), 
#but we can customize it as shown in line 28
print(a.nbytes)

#------accessing/changing specific element in row, array-----------

print(b[0, 3]) #get a specific element
print(b[0][:]) #get a specific row
print(b[0, :]) #alternative, a specific row
print(b[:,2]) #get a specific column 3rd column here
print(b[1, 1:5:2]) #2nd row, start element:end element : step
b[1,2] = 4 #replace
print(b)
b[:,2] =[1.2] #Replace a column
'''
#---------same rule for 3D data---------
'''
c = np.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])
print(c[:,1,:])
# All zeros matrix

d = np.zeros((2,3), dtype=float ) #dtype=int etc
print(d)

# Other same number
e = np.full((2,3), 2)
print(e)

#--------random numbers----------

f = np.random.rand(2,3) #2,3 matrix filled with random numbers
print(f)

#Copying array, be careful!!!!!!!!!!!!!

a = np.array([1,2,3])
b = a.copy() # dont do just b=a, it will not creat a separate array, copy is must
print(b)
b[0]=100
print(b)


#-------------Math operation with numpy
#https://numpy.org/doc/stable/reference/routines.html
'''
'''
a = np.ones((2,3))
b = np.full((3,2), 2)
print(a/2.)
print(a*2)
print(a+2)
print(a-2)
print(np.matmul(a,b))
print(a**2)
print(np.sin(a))

#----------statistics of array------------

g = np.array([[1, 2, 3], [4, 5, 6]])

print(np.max(g))
print(np.min(g))
print(np.mean(g))
print(np.sum(g))
print(np.max(g, axis=1))

#---------Re-organizing arrayts-----------------
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)
after = before.reshape(4, 2)
print(after)

#-----vertical stacking-------------
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

vstack = np.vstack([v1, v2])
print(vstack)

#---------horizontal stack----------

h1 = np.zeros([2, 4])
h2 = np.ones([2, 2])

hzstack = np.hstack([h1, h2])
print(hzstack)

#--------Reading data from text file------------
filedata = np.genfromtxt('mydata2.txt', delimiter = ',') #',' should be according to data
print(filedata)
'''

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:46:46 2025

@author: datta
"""

#--------------Reading files------------------


file = open("mydata.txt", "r") #"w", "a"-append information at the end the of the file, "r+"-read and write

print(file.readable())

print(file.readline()) #reading 1st line
print(file.readline()) #reading 2nd line
#....
#....


#print(file.read())
for i in file.readlines(): #Reading lines 
    print(i)

file.close()

#--------------Writing on to files--------------


file = open("mydata.txt", "a") #"w", "a"-append information at the end the of the file, "r+"-read and write
file.write("\n6.    12.")
file.close()

file = open("mydata1.txt", "w") #"w", "a"-append information at the end the of the file, "r+"-read and write


file.write("13.    14.\n")

file.close()


import numpy as np
data = np.loadtxt("data.dat")
t = data[:,0]
x = data[:,1]

# or
# t, x = np.loadtxt("data.dat",unpack=True)


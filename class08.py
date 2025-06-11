# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:17:47 2025

@author: datta
"""

import numpy as np
import matplotlib.pyplot as plt


# txt data read from a file and plot
filename = "time-displacement.txt"

data = np.loadtxt(filename)
#print(data)
time = data[:,0]
displacement = data[:,1]

plt.figure(figsize=(8, 5))
plt.plot(time, displacement, marker='o', linestyle='-', color='b', label='Displacement')
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Time vs. Displacement")
plt.legend()
plt.grid(True)
plt.savefig('time-dis.png', dpi=150)
plt.show()


#generate random numbers and plot hostogram 
#numbers=np.random.normal(0.,1.,1000) #
numbers=np.random.uniform(-4.,4.,1000)
bins = [-4,-3.5,-3.0,-2.5,-2.,-1.5,-1.,-.5,0, .5,1.,1.5,2.,2.5,3.,3.5,4.]
print(np.mean(numbers))
print(np.std(numbers))
plt.hist(numbers,bins)
plt.savefig('hist.png', dpi=150)
plt.show()

#-------------Image plot ( imshow )-----------------------------

#np.random.seed(19680801)

imdata = np.random.normal(0., 1., (101,101)) #Gaussian random number of mean 0, sd=1 of size (100*100)
imdata1 = np.random.normal(0., 1., (101,101))
print(np.mean(imdata))
print(np.std(imdata))


plt.imshow(imdata, origin='lower',cmap='coolwarm')#'plasma')#'viridis')#plt.cm.RdPu)#BuPu_r)




#plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

#cax = plt.axes([0.85, 0.1, 0.075, 0.8])
#plt.colorbar()#cax=cax)
#plt.colorbar(label="Intensity")
plt.show()




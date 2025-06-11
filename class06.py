# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:46:46 2025

@author: datta
"""

import random



#--------------Random number generation-----------------------
seq = [1,2,3,4,5,6,7,8,9]
#random.seed(100)
print(random.randint(1,10)) #Return a random integer N such that a <= N <= b
print(random.choice(seq)) #Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError
print(random.sample(seq,k=9))   #Return a k length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.
print(random.uniform(0., 1.)) #Return a random floating point number N such that a <= N <= b for a <= b 
mu=0.
sigma=1.
print(random.gauss(mu, sigma)) #Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function defined below

print(random.lognormvariate(mu, sigma)) #Log normal distribution. If you take the natural logarithm of this distribution, you’ll get a normal distribution with mean mu and standard deviation sigma. mu can have any value, and sigma must be greater than zero.



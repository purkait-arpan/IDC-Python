import random
import numpy as np
mu = 10.0
sigma = 1.0
x = [10.0]
y = [10.0]

for i in range (1, 1001):
  x.append(random.gauss(mu, sigma))
  y.append(random.gauss(mu, sigma))
  
  
np.savetxt("data.dat",np.column_stack((x,y)))


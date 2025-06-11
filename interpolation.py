from scipy.interpolate import lagrange
import numpy as np
x = np.array([0, 1, 2])
y = np.array([1, 3, 2])
poly = lagrange(x, y)
print(poly)

import numpy as np
import scipy 
f = lambda x: x**3

a = 0.
b = np.pi

x = np.linspace(a,b,100)
y = f(x)

area = scipy.integrate.quad(f,a,b)
print(area)

area = scipy.integrate.trapezoid(y,x)
print(area)

area = scipy.integrate.simpson(y,x)
print(area)

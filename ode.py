import numpy as np
import scipy
import matplotlib.pyplot as plt

def dydt(t,y):
  return -2.0*y
  
y0 = [1.]
t_span = (0,5)
t_ = np.linspace(0,5,1000)

solution = scipy.integrate.solve_ivp(dydt,t_span,y0,t_eval=t_)

plt.plot(solution.t,solution.y[0])
plt.show()

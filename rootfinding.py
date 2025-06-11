from scipy.optimize import bisect
f = lambda x: x**3 - x - 2.0
root1 = bisect(f,1.,2.,xtol=1e-12)
print(root1)


from scipy.optimize import newton
root2 = newton(f,1.)
print(root2)

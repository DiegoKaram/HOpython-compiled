import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(t, a, b):
    return a + b*t

datos = np.loadtxt("tabla.dat")
data = datos.reshape(1,20)

y=[]
x=[]
for i in range(0,20,2):
    x.append(data[0][i])
    y.append(data[0][i+1])

fitParams, fitCovariances = curve_fit(fitFunc, x, y)

plt.figure()
plt.ylabel('Y', fontsize = 16)
plt.xlabel('X', fontsize = 16)
plt.scatter(x,y)
plt.plot(x, fitFunc(x, fitParams[0], fitParams[1]))
plt.show()

plt.savefig('plot_scatter.pdf')

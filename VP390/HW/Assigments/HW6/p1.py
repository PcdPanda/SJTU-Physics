import numpy as np
import matplotlib.pyplot as plt
import math
t0=1
a=1e34
h=1.05e-34
m=9e-31
p0=1e30
t=30
x=np.linspace(-100,100,10000)
b=a*h*(1+t*2/(t0**2))**0.5
psi=math.e**(-(x-p0*m*t)**2/(b**2))/(b*math.pi**0.5)
title='The probability function at t=' + str(t)
plt.title(title)
plt.grid(1)
plt.plot(x,psi)
plt.show()


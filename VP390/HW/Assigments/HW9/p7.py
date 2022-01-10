import numpy as np
import matplotlib.pyplot as plt

Ef=5.49
kB=8.617e-5
Tf=Ef/kB
T=300
E = np.linspace(Ef,2*Ef,1000000)
f = 1/(2.717**((E-Ef)/(kB*T))+1)
print(sum((Ef/1000000)*f))
plt.title('Energy Distribution')
plt.plot(E,f)
plt.xlabel('Energy E_F')
plt.ylabel('f(E)')
plt.show()
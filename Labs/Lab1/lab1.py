import numpy as np 
import matplotlib.pyplot as plt

w = 10**(-np.linspace(1,10,10))
s = 3*w
x = np.linspace(1,len(w), len(w))

plt.semilogy(x,w, label = 'W vector')
plt.semilogy(x,s, label = 'S vector')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


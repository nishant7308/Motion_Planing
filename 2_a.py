import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10*np.pi, 200)  
r = 2.5*t
x = r * np.cos(t)
y = r * np.sin(t)

plt.xlabel('x---->')
plt.ylabel('y----->')
plt.axis('equal') 
plt.plot(x, y)
plt.show()
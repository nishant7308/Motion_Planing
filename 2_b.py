
import numpy as np

t = np.linspace(0, 10*np.pi, 200)  
r = 2.5*t
x = r * np.cos(t)
y = r * np.sin(t)

for i in range(1, len(x)):
    print("change in pose for x and theta are respectively x[",i,"]:",x[i] - x[i-1],"   ||   t[",i,"]: ",t[i] - t[i-1]) 
      
    



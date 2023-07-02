import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10*np.pi, 200)  
r = 2.5*t
x = r * np.cos(t)
y = r * np.sin(t)

for i in range(len(x)):
    plt.figure(figsize=(12, 12))  
    plt.plot(x, y, color='black')  
    plt.plot(x[i], y[i], 'ro') 
    
    r_rad = 8 
    r_len = 3  
    circle = plt.Circle((x[i],y[i]),r_rad,edgecolor='r', linewidth=.75, fill=False)
    plt.gca().add_patch(circle)
    
    l_x = 1.5*r_rad * np.cos(t[i]) + x[i]
    l_y = 1.5*r_rad * np.sin(t[i])+ y[i]
    plt.plot([x[i], l_x], [y[i], l_y], 'r-', linewidth=3)
    
    plt.xlabel('x---->')
    plt.ylabel('y---->')
    plt.axis('equal') 
    plt.grid(True)
    plt.savefig(f'loc{i}.png') 
    plt.close()

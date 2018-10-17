import matplotlib.pyplot as plt
import numpy as np
import math as m

Vo = int(input("Enter the velocity: "))
A = int(input("Enter the angle in degree: "))
g = 9.81

i = np.radians(A)
tmax = 2 * (Vo*m.sin(np.radians(A))/g)
t = np.linspace(0, tmax, num=1000) # Set time as 'continous' parameter.

x1 = []
y1 = []
for k in t:
    x = ((Vo*k)*np.cos(i)) # get positions at every point in time
    y = ((Vo*k)*np.sin(i))-((0.5*g)*(k**2))
    x1.append(x)
    y1.append(y)
p = [i for i, j in enumerate(y1) if j < 0] # Don't fall through the floor
for i in sorted(p, reverse = True):
    del x1[i]
    del y1[i]
plt.plot(x1, y1)

plt.title("Projectile Motion", fontsize = 24)
plt.xlabel("x-coordinate", fontsize = 18)
plt.ylabel("y-coordinate", fontsize = 18)

plt.show()

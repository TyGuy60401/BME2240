import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
xx, yy = np.meshgrid(x,y)

# g = xx*yy
# h = 1
# yp = 1/np.sqrt(np.e) * np.e**(x*x/2)
# g = yy*np.cos(xx)
# h = 1
# yp = (np.e**-np.sin(1))*(np.e**np.sin(x))
g = xx+yy
h = 1
yp = (-x-1)+((np.e*np.e**x)/3)
plt.plot(x, yp)
plt.ylim(-2,2)
plt.quiver(xx, yy, h, g)

plt.show()
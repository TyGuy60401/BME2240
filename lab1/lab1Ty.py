# This is Ty's file
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
xx, yy = np.meshgrid(x, y)

run = int(input("Which part of the lab? "))

if run == 1:
    # Part 1, dy/dx = xy
    g = xx*yy
    h = 1
    yp = 1/np.sqrt(np.e) * np.e**(x*x/2)
elif run == 2:
    # Part 2, dy/dx = y*cos(x)
    g = yy*np.cos(xx)
    h = 1
    yp = 0.431*np.e**(np.sin(x))
elif run == 3:
    # Part 3, dy/dx = x + y
    g = xx + yy
    h = 1
    # yp = -x + 2
    yp = -x - 1 + np.e*np.e**x/3
    yn = -x - 1
else:
    print("Invalid input")
    exit()

if run == 3:
    plt.plot(x, yp, x, yn)
else:
    plt.plot(x, yp)

plt.ylim(-2, 2)
plt.xlim(-2, 2)
plt.quiver(xx, yy, h, g)

plt.show()
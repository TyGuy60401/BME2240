import numpy as np
import matplotlib.pyplot as plt

# Initial Conditions
x0 = -2
y0 = 2.3
slope0 = x0/y0

# Set values for range and step size
xf = 2
n = 1001
deltax = (xf-x0)/(n-1)

# Create array for all x values
x = np.linspace(x0, xf, n)

# Create some arrays full of zeros
# for later use
y = np.zeros([n])
slope = np.zeros([n])

# Set the first value to our initial
# conditons
y[0] = y0
slope[0] = slope0

# Create loop to calculate next
# y-value based on previous coord
for i in range(1, n):
    y[i] = deltax*(x[i-1]/y[i-1]) + y[i-1]

# Now plot it
plt.plot(x, y, '.')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Solution of Differential Equation through y(-2)=1")
plt.show()
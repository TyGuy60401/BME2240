import numpy as np
import matplotlib.pyplot as plt

# We need to do everything twice

# Original from 1 to 2
# Initial Conditions
x0 = 1
y0 = 1.5
slope0 = x0/y0

# Set values for range and step size
xf = 2
deltax = 0.25
n = int((xf-x0)/(deltax) + 1)

# Create array for all x values
xright = np.linspace(x0, xf, n)

# Create some arrays full of zeros
# for later use
yright = np.zeros([n])
sloperight = np.zeros([n])

# Set the first value to our initial
# conditons
yright[0] = y0
sloperight[0] = slope0

# Create loop to calculate next
# y-value based on previous coord
for i in range(1, n):
    yright[i] = deltax*(xright[i-1]/yright[i-1]) + yright[i-1]


# Backwards from 1 to -2
x0 = 1
y0 = 1.5
slope0 = x0/y0

xf = -2
deltax = 0.25
n = int((x0-xf)/(deltax)+1)

xleft = np.linspace(x0, xf, n)

yleft = np.zeros([n])
slopeleft = np.zeros([n])

yleft[0] = y0
slopeleft[0] = slope0

for i in range(1, n):
    yleft[i] = -deltax*(xleft[i-1]/yleft[i-1]) + yleft[i-1]

# x = xleft + xrightt
x = np.append(xleft, xright)
# y = yleft + yright
y = np.append(yleft, yright)

xx = np.linspace(-2, 2, 1001)

# Now plot it
plt.plot(x, y, '.')
plt.plot(xx, np.sqrt(xx**2+1.25), c="green")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Solution of Differential Equation through y(2)=1.5")
plt.show()
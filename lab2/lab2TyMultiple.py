# This is Ty's file!
import numpy as np
import matplotlib.pyplot as plt

foutname = input("File name: ")
fout = open(foutname, 'w')


# Initial Conditions
# Part 1
# x0 = -2
# y0 = 2
# slope0 = x0*x0*y0-x0*y0

#Part 2
# x0 = 0
# y0 = 1
# slope0 = 2*y0-np.e**(-4*x0)

# Part 3
x0 = 0
y0 = 1
slope0 = y0*np.cos(x0)-y0/4

# Set values for range and step size
xf = 10
# n = 1001
# deltax = (xf-x0)/(n-1)
# Part 1 and 2
# deltaxList = [0.2, 0.1, 0.05]

# Part 3
deltaxList = [0.2, 0.1, 0.05, 0.01, 0.005, 0.002]
deltaxList = [0.2, 0.002]


for deltax in deltaxList:
    n = int((xf-x0)/(deltax) + 1)

    # Create array for all x values
    x = np.linspace(x0, xf, n)

    # Create some arrays full of zeros
    # for later use
    y = np.zeros([n])
    yfin = np.zeros([n])
    slope = np.zeros([n])

    # Set the first value to our initial
    # conditons
    y[0] = y0
    yfin[0] = y0
    slope[0] = slope0



    # Create loop to calculate next
    # y-value based on previous coord
    fout.write('x,y,dy/dx\n')
    fout.write('%.3f,%.3f,%.3f\n' % (x0, y0, slope0))
    for i in range(1, n):
        # Part 1 code
        # y[i] = deltax*(x[i-1]**2*y[i-1]-x[i-1]*y[i-1]) + y[i-1]
        # slope = (x[i]**2*y[i]-x[i]*y[i]) 

        # Part 2 code
        # y[i] = deltax*(2*y[i-1]-np.e**(-4*x[i-1])) + y[i-1]
        # slope = (2*y[i]-np.e**(-4*x[i]))

        # Part 3 code
        y[i] = deltax*(y[i-1]*np.cos(x[i-1])-y[i-1]/4) + y[i-1]
        slope = (y[i]*np.cos(x[i])-y[i]/4)
        yfin[i] = np.e**(np.sin(x[i]) - 0.25*x[i])
        fout.write('%.3f,%.3f,%.3f\n' % (x0+i*deltax, y[i], slope))

    # Now plot it
    plt.plot(x, y, '.')
plt.plot(x, yfin, c="green")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
# Part 1
# plt.title("Solution of dy/dx = x^2y-xy through y(-2)=2")

# Part 2
# plt.title("Solution of dy/dx = 2y - e^-4x through y(0)=1")

# Part 3
plt.title("Solution of dy/dx = ycos(x) - y/4 through y(0)=1")
plt.show()
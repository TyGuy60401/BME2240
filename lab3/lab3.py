#!/usr/bin/env/python3
import numpy as np
import matplotlib.pyplot as plt

fout = open("output.csv", 'w')

def printLine(t=0, yEuler=0, k1Euler=0, yMidpoint=0, k1Mid=0, k2Mid=0, yRK=0, k1RK=0, k2RK=0, k3RK=0, k4RK=0):
    fStr1 = "%.1f"
    fStr2 = "%f"
    longStr = fStr1 + ',' + (fStr2 + ',') * 10
    return longStr % (t, yEuler, k1Euler, yMidpoint, k1Mid, k2Mid, yRK, k1RK, k2RK, k3RK, k4RK)

def func(t, y):
    return y*t**3 - 1.5*y

# Initial Conditions
t0 = 0
y0 = 1
k1 = y0*t0**3-1.5*y0

# Set values for range and step size
tf = 4
deltat = 0.5
n = int((tf-t0)/deltat + 1)

# Create array for the t values
t = np.linspace(t0, tf, n)
# Create Euler arrays
yEuler = np.zeros([n])
k1Euler = np.zeros([n])

# Create Midpoint arrays
yMidpoint = np.zeros([n])
k1Midpoint = np.zeros([n])
k2Midpoint = np.zeros([n])

# Create RK4 arrays
yRK4 = np.zeros([n])
k1RK4 = np.zeros([n])
k2RK4 = np.zeros([n])
k3RK4 = np.zeros([n])
k4RK4 = np.zeros([n])


# Set the first value of arrays to our initial conditions
# dy/dt = yt^3 -1.5y
yEuler[0] = y0
k1Euler[0] = k1

yMidpoint[0] = y0
k1Midpoint[0] = k1
k2Midpoint[0] = (y0+deltat/2*k1) * (t0+deltat/2)**3 - 1.5*(y0+deltat/2*k1)

yRK4[0] = y0
k1RK4[0] = k1
k2RK4[0] = func(t0 + deltat/2, y0 + deltat/2*k1)
k3RK4[0] = func(t0 + deltat/2, y0 + deltat/2*k2RK4[0])
k4RK4[0] = func(t0 + deltat, y0 + deltat*k3RK4[0])


# Create loop for all the output

fout.write("t,Euler,k1,Midpt,k1,k2,RK4,k1,k2,k3,k4")
fout.write('\n')
fout.write(printLine(t[0],yEuler[0],k1Euler[0],yMidpoint[0],k1Midpoint[0],k2Midpoint[0], yRK4[0], k1RK4[0],k2RK4[0],k3RK4[0],k4RK4[0]))
fout.write('\n')
for i in range(1, n):
    # dy/dt = yt^3 -1.5y

    # Euler's method section
    yEuler[i] = deltat*( k1Euler[i-1] ) + yEuler[i-1]
    k1Euler[i] = func(t[i], yEuler[i])

    # Midpoint section
    yMidpoint[i] = deltat*( k2Midpoint[i-1] ) + yMidpoint[i-1]
    k1Midpoint[i] = func(t[i], yMidpoint[i])
    k2Midpoint[i] = func(t[i] + deltat/2, yMidpoint[i] + deltat/2*k1Midpoint[i])

    # RK4 sections
    yRK4[i] = deltat*( k1RK4[i-1]/6 + k2RK4[i-1]/3 + k3RK4[i-1]/3 + k4RK4[i-1]/6) + yRK4[i-1]
    k1RK4[i] = func(t[i], yRK4[i])
    k2RK4[i] = func(t[i] + deltat/2, yRK4[i] + deltat/2*k1RK4[i])
    k3RK4[i] = func(t[i] + deltat/2, yRK4[i] + deltat/2*k2RK4[i])
    k4RK4[i] = func(t[i] + deltat, yRK4[i] + deltat*k3RK4[i])


    fout.write(printLine(t[i],yEuler[i],k1Euler[i],yMidpoint[i],k1Midpoint[i],k2Midpoint[i], yRK4[i], k1RK4[i],k2RK4[i],k3RK4[i],k4RK4[i]))
    fout.write('\n')

plt.plot(t, yEuler, t, yMidpoint, t, yRK4)
plt.yscale("symlog")
plt.show()

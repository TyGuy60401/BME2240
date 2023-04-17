import numpy as np
import matplotlib.pyplot as plt

# Make the time values t
t0 = 0
tf = 60
num = 600
deltat = (tf-t0/num)
t = np.linspace(t0, tf, num+1)

# Make zero arrays
x = np.zeros([num+1])
x_k1 = np.zeros([num+1])
x_k2 = np.zeros([num+1])
x_k3 = np.zeros([num+1])
x_k4 = np.zeros([num+1])

u = np.zeros([num+1])
u_k1 = np.zeros([num+1])
u_k2 = np.zeros([num+1])
u_k3 = np.zeros([num+1])
u_k4 = np.zeros([num+1])

# Set the initial conditions
x[0] = 0
x_k1[0] = 0
x_k2[0] = 0
x_k3[0] = 0
x_k4[0] = 0

u[0] = 0
u_k1[0] = 0
u_k2[0] = 0
u_k3[0] = 0
u_k4[0] = 0

def f1(x, u):
    m = 0.9
    g = -9.81
    c = 0.001
    k = 45
    return (m*g - c*u - k*x)/m


# Create the big ol' loop
for i in range(1, num):
    u[i] = deltat*( u_k1[i-1]/6 + u_k2[i-1]/3 + u_k3[i-1]/3 + u_k4[i-1]/6) + u[i-1]
    u_k1[i] = f1(x[i-1], u[i])
    u_k2[i] = f1(x[i-1] + deltat/2, u[i] + deltat/2*u_k1[i])
    u_k3[i] = f1(x[i-1] + deltat/2, u[i] + deltat/2*u_k2[i])
    u_k4[i] = f1(x[i-1] + deltat, u[i] + deltat*u_k3[i])

    x[i] = deltat*( x_k1[i-1]/6 + x_k2[i-1]/3 + x_k3[i-1]/3 + x_k4[i-1]/6) + x[i-1]
    x_k1[i] = u[i]
    x_k2[i] = u[i] + deltat/2*x_k1[i]
    x_k3[i] = u[i] + deltat/2*x_k2[i]
    x_k4[i] = u[i] + deltat*x_k3[i]

plt.plot(t, x, label="position")
plt.show()
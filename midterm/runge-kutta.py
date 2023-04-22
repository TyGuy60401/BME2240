import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # RK4 Approximation
    t = np.linspace(0, 60, 600)
    h = t[1]-t[0]
    x0 = 0
    v0 = -9.81/0.9
    x = runge_kutta_4(f, x0, v0, h, t)

    analytical = analyze(t, 1.1, 1.1, 0.011, 6.1)

    data = pd.read_csv('output-final.txt', index_col='time', sep=' ')
    data['position'] = data['position'].map(lambda x: x/100 - 4.2)

    plt.xlabel(r"Time $[s]$")
    plt.ylabel(r"Distance $[m]$")
    plt.plot(t, x, label="RK4 Approx.", color="xkcd:red")
    plt.plot(t, analytical, label="Analytical", color="xkcd:azure")
    plt.plot(data, '.', label="Measured Data", color="xkcd:faded green")
    plt.title("RK4, Measured Data - Mass on a Spring")
    plt.legend()
    # plt.savefig("./imgs/output_img.png")
    plt.show()

def runge_kutta_4(f, x0, u0, h, t):
    x = np.zeros(len(t))
    u = np.zeros(len(t))
    x[0] = x0
    u[0] = u0
    for i in range(1, len(t)):
        k1x = h * u[i-1]
        k1u = h * (f(t[i-1], x[i-1], u[i-1]))

        k2x = h * (u[i-1] + 0.5 * k1u)
        k2u = h * (f(t[i-1] + 0.5 * h, x[i-1] + 0.5 * k1x, u[i-1] + 0.5 * k1u))
        
        k3x = h * (u[i-1] + 0.5 * k2u)
        k3u = h * (f(t[i-1] + 0.5 * h, x[i-1] + 0.5 * k2x, u[i-1] + 0.5 * k2u))

        k4x = h * (u[i-1] + k3u)
        k4u = h * (f(t[i-1] + h, x[i-1] + k3x, u[i-1] + k3u))

        x[i] = x[i-1] + (k1x + 2*k2x + 2*k3x + k4x) / 6
        u[i] = u[i-1] + (k1u + 2*k2u + 2*k3u + k4u) / 6
    return x

def f(t, x, u):
    return -45*x - 0.0175*u - 0.9*9.81

def analyze(t, c1, c2, alpha, beta):
    return c1*np.e**(-alpha * t)*np.cos(beta*t) + c2*np.e**(-alpha * t)*np.sin(beta*t) - 0.2

if __name__ == '__main__':
    main()

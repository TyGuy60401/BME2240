import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    t = np.linspace(0, 60, 600)
    h = t[1]-t[0]
    x0 = 0
    v0 = -9.81/0.9
    x = runge_kutta_4(f, x0, v0, h, t)

    # print(x)
    plt.plot(t, x)

    # Data from file
    data = pd.read_csv('output-final.txt', index_col='time', sep=' ')
    data['position'] = data['position'].map(lambda x: x/100 - 4.2)
    plt.plot(data)
    # data.plot()
    plt.show()

def runge_kutta_4(f, x0, v0, h, t):
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = x0
    v[0] = v0
    for i in range(1, len(t)):
        k1x = h * v[i-1]
        k1v = h * (f(t[i-1], x[i-1], v[i-1]))
        k2x = h * (v[i-1] + 0.5 * k1v)
        k2v = h * (f(t[i-1] + 0.5 * h, x[i-1] + 0.5 * k1x, v[i-1] + 0.5 * k1v))
        k3x = h * (v[i-1] + 0.5 * k2v)
        k3v = h * (f(t[i-1] + 0.5 * h, x[i-1] + 0.5 * k2x, v[i-1] + 0.5 * k2v))
        k4x = h * (v[i-1] + k3v)
        k4v = h * (f(t[i-1] + h, x[i-1] + k3x, v[i-1] + k3v))
        x[i] = x[i-1] + (k1x + 2*k2x + 2*k3x + k4x) / 6
        v[i] = v[i-1] + (k1v + 2*k2v + 2*k3v + k4v) / 6
    return x

def f(t, x, v):
    return -45*x - 0.0175*v - 0.9*9.81

if __name__ == '__main__':
    main()

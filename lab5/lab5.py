import matplotlib.pyplot as plt
from scipy import signal

def main():
    """Plotting a transfer function, and displaying the zeroes and poles with x and o """
    res = 470
    cap = 0.1E-6
    RC = res*cap
    A = 0
    B = 0
    C = 5
    D = RC
    E = 1
    F = 0
    sys = signal.TransferFunction([A,B,C],[D,E,F])
    w, mag, phase = signal.bode(sys)
    plt.figure()
    plt.semilogx(w,mag) #magnitude
    plt.figure()
    plt.semilogx(w,phase) #phase
    plt.show()

if __name__=="__main__":
    main()
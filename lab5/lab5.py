import matplotlib.pyplot as plt
from scipy import signal

def main():
    res = 470
    cap = 0.1E-6
    RC = res*cap
    A = 0
    B = 0
    C = 1
    D = 0
    E = RC
    F = 1
    sys = signal.TransferFunction([A,B,C],[D,E,F])
    w, mag, phase = signal.bode(sys)
    plt.figure()
    plt.semilogx(w,mag) #magnitude
    plt.title("Magnitude of RC Circuit")
    plt.figure()
    plt.semilogx(w,phase) #phase
    plt.title("Phase Angle of RC Circuit")

    res = 470
    cap = 0.01E-6
    induc = 100E-3
    RC = res*cap
    LC = induc*cap
    A = 0
    B = 0
    C = 1
    D = LC
    E = RC
    F = 1
    sys = signal.TransferFunction([A,B,C],[D,E,F])
    w, mag, phase = signal.bode(sys)
    plt.figure()
    plt.semilogx(w,mag) #magnitude
    plt.title("Magnitude of RLC Circuit")
    plt.figure()
    plt.semilogx(w,phase) #phase
    plt.title("Phase Angle of RLC Circuit")
    plt.show()

if __name__=="__main__":
    main()
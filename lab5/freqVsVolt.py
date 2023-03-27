import matplotlib.pyplot as plt
import numpy as np
import sys

def main(argv):
    if len(argv) == 1:
        graphChoice = int(input("Which graph, 1 or 2? "))
    else:
        graphChoice = int(argv[1])

    if graphChoice == 1:
        freq = np.array([200, 500, 1000, 2000, 5000, 10000, 20000, 100000])
        volt = np.array([5.11, 5.07, 4.86, 4.3, 2.8, 1.65, 0.92, 0.28])
        plt.title("Voltage vs Frequency - RC Series Circuit\n - Measured Values - ")
        # plt.savefig("freqVsVolt.png")
    elif graphChoice == 2:
        freq = np.array([1000, 1500, 2000, 3000, 4000, 5000, 6000, 7500, 10000, 20000, 50000, 75000, 100000])
        volt = np.array([5.5, 5.8, 6.3, 7.9, 12.2, 17.2, 8.9, 4, 1.9, 0.6, 0.35, 0.35, 0.3])
        plt.title("Voltage vs Frequency - RLC Series Circuit\n - Measured Values - ")
    plt.plot(freq, volt, '.')
    plt.xlabel(r"Frequency $[Hz]$")
    plt.ylabel(r"Voltage $[V]$")
    plt.semilogx()
    if len(argv) == 3:
        plt.savefig(argv[2])
    plt.show()



if __name__ == '__main__':
    main(sys.argv)
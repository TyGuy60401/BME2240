import numpy as np
import matplotlib.pyplot as plt
import h5py

import linear_algebra as la

def main():

    with h5py.File("data.h5", "r") as hf:
        print(hf.keys())
        si = np.array(hf.get("si_images"))
        bvals = np.array(hf.get("bvals"))
        gradients = np.array(hf.get("gradient"))
        s0 = np.array(hf.get("s0_image"))
    


    try:
        FA = np.loadtxt('FA-out-0.txt')
    except:
        print("File not found, calculating new array")
    else:
        plt.imshow(1-FA, cmap='Greys')
        plt.show()
        return

    FA = np.zeros(s0.shape)
    for m in range(s0.shape[0]):
        for n in range(s0.shape[1]):
            inner = si[m,n,:]/(s0[m,n]+1e-16)
            if np.max(inner) < 1e-16:
                FA[m,n] = 0
                continue
            y = -np.log(inner).squeeze()/bvals
            dvals = la.linear_least_squares(gradients.T, y)
            dx = dvals[0]
            dy = dvals[1]
            dz = dvals[2]
            D = np.array([[dx*dx, dx*dy, dx*dz],
                          [dx*dy, dy*dy, dy*dz],
                          [dx*dz, dy*dz, dz*dz]])
            w, v = la.eigen(D, MAX_ITER=2000)
            l0, l1, l2 = w
            FA[m,n] = np.sqrt(((l0-l1)**2 + (l0-l2)**2 + (l1-l2)**2)/ (2*(l0*l0 + l1*l1 + l2*l2)))


            if n % 20 == 0:
                progressBar(m, s0.shape[0], extra=str(dvals) + "(%3d, %3d)  %.2f " % (m,n, FA[m,n]))

    print("\n\n")
    np.savetxt('FA-out.txt', FA)
    plt.imshow(1-FA, cmap='Greys')
    plt.show()
    



def progressBar(val, maxVal, extra="", length=20):
    portion = int(val/maxVal*length)
    if extra == "":
        extraPortion = ""
    else:
        extraPortion = " - " + extra
    print("[","#"*portion, " "*(length-portion-1), "]", extraPortion, sep="", end='\r')



if __name__ == '__main__':
    main()
import numpy as np
import h5py

def main():

    with h5py.File("data.h5", "r") as hf:
        print(hf.keys())
        si = np.array(hf.get("si_images"))
        b = np.array(hf.get("bvals"))
        gradients = np.array(hf.get("gradient"))
        s0 = np.array(hf.get("s0_image"))

    for k in range(len(gradients)):
        
        continue

    if True:
        print("SI:", si, "\n")
        print("B: ", b, "\n")
        print("g: ", gradients, "\n")
        print("s0:", s0, "\n")

        print(si[0][0])

        print(len(b))
        print(len(si))
        print(si.shape)
        print(gradients.shape)
        print(s0.shape)
        print(s0[65][60])



if __name__ == '__main__':
    main()
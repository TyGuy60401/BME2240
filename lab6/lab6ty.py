import numpy as np
import sys

def main(argv):
    A = np.array([[-1100,   100,  1000],
                  [  100, -1430,   330],
                  [ 1000,   330, -2230]])
    A_inv = np.linalg.inv(np.matrix(A))

    S = [-10, 0, 0]
    x = np.dot(A_inv, S)
    print("Solution matrix:",x, sep='\n')
    print("A inverse:",A_inv, sep='\n')
    return

if __name__ == '__main__':
    main(sys.argv)
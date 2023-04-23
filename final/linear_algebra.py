import numpy as np
import sys

def main(argv):
    V = np.array([1, 0, 1])
    # print(normalize(V))
    a = np.array([[1, 1, 2],
                  [0, -1, 2],
                  [1, -1, 1]])
    print(get_e(a, 1))
    # print(np.subtract(a, 1))
    return

def qrgs(A):
    """Gram-Schmidt QR decomposition that decomposes A such
    that A = QR
    
    Parameters
    ----------
    A : ndarray
        input Array A to decompose with size MxN where M >= N
    
    Returns
    -------
    Q : ndarray
        orthogonal matrix Q size MxN
    R : ndarray
        upper triangular matrix R size NxN"""
    
    # We need to calculate the Q, might use some recursion 👀

    return

def normalize(V):
    """Normalize a vector V to its unit vector."""
    radicand = 0
    # Calculate the length
    for val in V:
        radicand += val*val
    print(np.abs(V))
    length = np.sqrt(radicand)
    return V/length


def get_e(A, n):
    """Returns a vector from matrix A which will be used in
    the calculation of Q in the Gram-Schmidt decomposition"""
    # un = an - (dot(an, en-1))*en-1 - (dot(an,en-2))*en-2 - ... - (dot(an,e1))*e1
    if n == 1:
        u = A[:,0:1]
        e = normalize(u)
        return e
    elif n > 1:
        an = A[:, n-1:n]
        # subtrahend = 
        # u =  


if __name__ == '__main__':
    main(sys.argv)
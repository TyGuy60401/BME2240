import numpy as np
import sys

def main(argv):
    a = np.array([[1, 1, 2],
                  [0, -1, 2],
                  [1, -1, 1]])
    b = np.array([1, 10, 1])
    # Q, R = qrgs(a)
    print(linear_least_squares(a, b))
    return

def linear_least_squares(A, b):
    """QR-based linear least squares to solve Ax=b
    
    Parameters
    ----------
    A : ndarray
        Skinny (MxN where M >= N) matrix
    B : ndarray
        1D array
    
    Returns
    -------
    x : ndarray
        1D solution array
    """
    # Ax = b
    # Rx = Q^T b
    Q, R = qrgs(A)
    
    rhs = np.flip(np.matmul(Q.T, b))
    print(rhs)
    print(np.flip(R))
    x = np.array([])
    R_flip = np.flip(R)
    for i in range(len(R_flip)):
        sol = rhs[i]
        j = 0
        for val in x:
            sol -= R_flip[i, j]*val
            j += 1
        sol /= R_flip[i, j]
        x = np.append(x, sol)
    return np.flip(x)

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
    Q = np.zeros(A.shape)
    for i in range(len(A[0])):
        Q = np.concatenate((Q[:,0:i], get_e(A, i+1), Q[:,i+1:]), axis=1)
    
    # Making the R matrix
    n = A.shape[1]
    R = np.zeros((n,n))
    for i in range(len(R)):
        for j in range(len(R[i])):
            if j >= i:
                v1 = np.squeeze(A[:,j:j+1])
                v2 = np.squeeze(get_e(A, i+1))
                R[i,j] = np.dot(v1, v2)

    return Q, R

def normalize(V):
    """Normalize a vector V to its unit vector."""
    radicand = 0
    # Calculate the length
    for val in V:
        radicand += val*val
    # print(np.abs(V))
    length = np.sqrt(radicand)
    return V/length


def get_e(A, n):
    """Returns a vector from matrix A which will be used in
    the calculation of Q in the Gram-Schmidt decomposition"""
    # un = an - (dot(an, en-1))*en-1 - (dot(an,en-2))*en-2 - ... - (dot(an,e1))*e1
    if n == 1:
        u = A[:,0:1]
    elif n > 1:
        an = A[:, n-1:n]
        u = an
        while n > 1:
            en_1 = get_e(A, n-1)
            v1 = np.squeeze(an)
            v2 = np.squeeze(en_1)
            val = np.dot(v1, v2)
            
            u = np.subtract(u, val * en_1)
            n -= 1
    
    e = normalize(u)
    return e


if __name__ == '__main__':
    main(sys.argv)
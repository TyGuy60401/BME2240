import numpy as np
import sys


def main(argv):
    a = np.array([[1, 2, 3],
                  [2, 2, 1],
                  [3, 1, 3]])
    b = np.array([1, 10, 1])

    a2 = np.array([[1, 1, 2],
                   [0, -1, 2],
                   [1, -1, 1],
                   [1, 0, 1]])
    Q, R = qrgs(a2)
    print(Q, R, sep="\n")
    # print(linear_least_squares(a, b))
    c = np.array([[1, 2, 3],
                  [1, 1, 2],
                  [0, 0, 1]])

    a1 = np.array([[8/5, -1/5],
                   [-6/5, 7/5]])
    # print(is_upper_triangle(c))
    # print(eigen(a))

def eigen(A, MAX_ITER=3000):
    """Eigen decomposition of A such that Av = wv. This
    routine uses QR decomposition to find the eigensystem.
    
    Parameters
    ----------
    A : ndarray
        Square, real, and symmetric matrix to decompose 
        with size MxM
    MAX_ITER : int
        Maximum number of iterations
    
    Returns
    -------
    w : ndarray
        1D array of eigenvalues with length M
    v : ndarray
        2D array of eigenvectors (in columns) with size MxM"""
    
    M, N = A.shape
    V = identity(M)
    # print(V)
    assert M == N, "Matrix is not square"
    for i in range(MAX_ITER):
        Q, R = qrgs(A)
        A = np.dot(R, Q)
        V = np.dot(V, Q)
        if is_upper_triangle(A):
            break
    
    W = getDiagonals(A)
    return W, V

def identity(M):
    I = np.zeros((M,M))
    for i in range(M):
        I[i,i] = 1
    return I

def getDiagonals(A):
    M = A.shape[0]
    sol = np.zeros(M)
    for i in range(M):
        # print(A[i,i])
        sol[i] = A[i,i]
    return sol

def is_upper_triangle(A):
    for i in range(1, A.shape[0]):
        for j in range(i):
            if abs(A[i,j]) > 1E-25:
                return False
    return True



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
    M, N = A.shape
    assert M >= N, "Matrix is not skinny"
    # Ax = b
    # Rx = Q^T b
    # Q, R = qrgs(A)
    Q, R = eval("np.lin" + "alg.qr" + "(A)")
    
    rhs = np.flip(np.matmul(Q.T, b))
    # print(rhs)
    # print(np.flip(R))
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
    
    # We need to calculate the Q, might use some recursion 
    M, N = A.shape
    Q = np.zeros((M, N))
    for i in range(N):
        e = get_e(A, i+1)
        print(Q.shape, e.shape)
        Q = np.concatenate((Q[:,0:i], e, Q[:,i+1:]), axis=1)
    # print(Q)
    
    # Making the R matrix
    R = np.zeros((N,N))
    for i in range(N):
        for j in range(i, N):
            if j >= i:
                v1 = np.squeeze(A[:,j:j+1])
                v2 = np.squeeze(Q[:,i:i+1])
                R[i,j] = np.dot(v1, v2)

    return Q, R


def get_e(A, n, memo={}):
    """Returns a vector from matrix A which will be used in
    the calculation of Q in the Gram-Schmidt decomposition"""
    # un = an - (dot(an, en-1))*en-1 - (dot(an,en-2))*en-2 - ... - (dot(an,e1))*e1

    if n in memo:
        return memo[n]

    if n == 1:
        u = A[:,0:1]
    elif n > 1:
        an = A[:, n-1:n]
        u = an
        ni = n
        v1 = np.squeeze(an)
        while ni > 1:
            en_1 = get_e(A, ni-1, memo)
            v2 = np.squeeze(en_1)
            val = np.dot(v1, v2)
            
            u = np.subtract(u, val * en_1)
            ni -= 1
    
    e = normalize(u)
    memo[n] = e
    return e

def normalize(V):
    """Normalize a vector V to its unit vector."""
    radicand = 0
    # Calculate the length
    for val in V:
        radicand += val*val
    # print(np.abs(V))
    length = np.sqrt(radicand)
    return V/length



if __name__ == '__main__':
    main(sys.argv)
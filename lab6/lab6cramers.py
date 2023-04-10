import numpy as np
import sys

def main(argv):
    A = np.array([[-1100,   100,  1000],
                  [  100, -1430,   330],
                  [ 1000,   330, -2230]], dtype='int64')
    S = np.array([[-10, 0, 0]], dtype='int64')

    solution = cramer(A, S)
    print(solution)

def cramer(A, S):
    det_A = calc_det(A)
    solution = []
    for i in range(len(A[0])):
        mat = np.concatenate((A[:,0:i], S.T, A[:,i+1:]), axis=1)
        val = calc_det(mat) / det_A
        solution.append(val)
    return np.array(solution)

def calc_det(A):
    n = len(A[0])
    val = 0
    if (n == 1):
        return A[0]
    elif (n == 2):
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        for i in range(len(A[0])):
            val += A[0][i] * calc_det(np.concatenate((A[1:,0:i], A[1:,i+1:]), axis=1)) * (int(i%2 == 0) * 2 - 1)
    return val

if __name__ == '__main__':
    main(sys.argv)
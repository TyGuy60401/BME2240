import numpy as np
import sys

def main(argv):
    A = np.array([[-1100,   100,  1000],
                  [  100, -1430,   330],
                  [ 1000,   330, -2230]], dtype='int64')
    S = np.array([[-10, 0, 0]], dtype='int64')

    det = calc_det(A)
    D_x = np.concatenate((S.T,A[:,1:]), axis=1)
    D_y = np.concatenate((A[:,0:1], S.T, A[:,2:]), axis=1)
    D_z = np.concatenate((A[:,0:2], S.T), axis=1)
    x = calc_det(D_x) / det
    y = calc_det(D_y) / det
    z = calc_det(D_z) / det
    print(np.array([x,y,z]))
    
    return

def calc_det(A):
    n = len(A[0])
    if (n == 1):
        return A[0]
    elif (n == 2):
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        val = 0
        for i in range(len(A[0])):
            sub1 = A[1:,0:i]
            sub2 = A[1:,i+1:]
            sub = np.concatenate((sub1, sub2), axis=1)
            even = int(i%2 == 0) * 2 - 1
            val += A[0][i] * calc_det(sub) * even
    return val


if __name__ == '__main__':
    main(sys.argv)
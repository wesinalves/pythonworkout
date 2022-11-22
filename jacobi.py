"""
Jacobi'a method to solve linear equation system
Ax = b

x_(k+1) = D^-1(b - (L+U)x_k)
T = -D^-1(L+U)
C = D^-1b

A, initial x, b and max iter are given
find x estimated until converge or max iter

converge: Ax - b ~ 0

by Wesin Ribeiro
22/11/2022
100 days of python code
07/99
"""

def is_close(vetx, vety):
    close = False
    n = len(vetx)    
    for i in range(n):
        if abs(vetx[i] - vety[i]) < 0.0001:
            close = True
        else:
            close = False
    
    return close

def jacobi_method(A, b, x, n, max_iteration):
    x_new = [0]*len(x)

    for _ in range(max_iteration):    
        for i in range(n):
            sig = 0
            for j in range(n):
                if j != i:
                    sig = sig + A[i][j] * x[j]
            x_new[i] = (b[i] - sig) / A[i][i]   
        
        if is_close(x, x_new):
            break

        x = x_new.copy()
    
    return x


def main():
    A = [[10, -1, 2, 0], 
        [-1, 11, -1, 3], 
        [2, -1, 10, -1], 
        [0, 3, -1, 8]]
    b = [6, 25, -11, 15]
    x0 = [0, 0, 0, 0]
    
    max_iteration = 100

    n = len(A[0])
    x = jacobi_method(A,b,x0,n,max_iteration)
    print(x)

main()







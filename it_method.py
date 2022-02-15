
import numpy as np
from matrix_norm import *
from vect import *

def it_method(a):
    for i in range(len(a)):
        a[i] = -(a[i] / a[i][i])
        a[i][i] = 0
    a = np.round(a, 4)
    print (a)
    print("%%%%%")
    b = matrix_norm(a[:, 0: len(a)], '1')
    B = a[:, 0: len(a)]
    i = 0
    e = 0.001
    answ = 1
    x = [0]*len(a) 
    # x[0] = np.sum(B[0:1] * 0) - a[0][-1]

    if b < 1:
            for i in range (len(a)):
                x[i] = np.sum(B[i:i+1] * (1.2)) - a[i][-1]
                # x^k+1) = B(x)^(k) + C
    print(x)          
    # print (b)
    # print(a[:, 0: len(a)])
    # print (a[0][-1])

# m = int(input("Number of m:\n"))
# n = int(input("Number of n:\n"))
# # p = input("Print: 1 or 'inf'\n")
# a = np.arange(m * n, dtype='float').reshape(m, n)
a = np.array([[6.25, -1, 0.5, 7.5],
              [-1, 5, 2.12, -8.68],
              [0.5, 2.12, 3.6, -0.24]], dtype='float')
# for i in range(m):
#     print("Enter", i + 1, "row:")
#     a[i] = np.asarray(input().split()).astype(float)
it_method(a)


# 6.25 -1 0.5 7.5
# -1 5 2.12 -8.68
# 0.5 2.12 3.6 -0.24
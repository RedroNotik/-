# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:30:06 2021

@author: timof
"""

import numpy as np

def matrix_norm(A, p):
    A = np.absolute(A) 
    norm = 0    
    if (p == '1'):
        for i in range(len(A)):
            if np.sum(A[i]) > norm:
                norm = np.sum(A[i])
    elif (p == 'inf'):
        A = np.transpose(A)
        for i in range(len(A)):
            if np.sum(A[i]) > norm:
                norm = np.sum(A[i])
    return(norm)    
    
#m = int(input("Enter matrix size MxM:\n"))
#p = input("Print: 1 or 'inf'\n")
#a = np.arange(m*m).reshape(m,m)
#for i in range(m):
  #  print ("Enter", i + 1, "row:")
  #  a[i] = np.asarray(input().split()).astype(float)
    
#norm = matrix_norm(a, p)
#print("Norm is:", norm)  
        
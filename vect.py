# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def vector_norm(a, p):
    a = a.absolute(a)
    norm = -1
    if (p == 'inf'):
        norm = np.max(a)
    elif (int(p) <= 0):
        print ("Incorrect p")
    else: 
        p = int(p)
        norm = np.power(np.sum(np.power(a,p)), 1/p)
    return (norm)


# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:48:37 2024

@author: Kali Linux
"""
import numpy as np
import cholesky as ck
import forwardSubstitution as fs
import backwardSubstitution as bs

def LSCH(A, b):
    m, n = A.shape
    L, U = ck.cholesky(A)
    z = fs.forwardSubstitution(L, b)
    x = bs.backwardSubstitution(U, z)
    
    return x

A = np.array([[2., -1], [-1, 3]])
b = np.array([[1, 2]]).T
x = LSCH(A, b)

print(f"The solution x: \n\n {x}")
    
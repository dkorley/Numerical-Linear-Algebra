# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:24:53 2024

@author: Kali Linux
"""

import numpy as np

def cholesky(A):
    m = A.shape[0]
    n = A.shape[1]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    #check if matrix is square
    if m != n:
        raise ValueError("Matrix is not square")
    
    #check if matrix is HPD
    eigenvalue = np.linalg.eigvals(A)
    if np.min(eigenvalue) < 0:
        raise ValueError("Matrix is not positive definite")
    
    for j in range(n):
        U[j, j] = np.sqrt(A[j, j])
        L[j, j] = U[j, j]
        
        for i in range(j + 1, n):
            L[i, j] = A[i, j] / U[j, j]
            U[j, i] = L[i, j]
            
        for k in range(j+1, n):
            for i in range(k, n):
                A[i, k] -= np.dot(L[i, j], U[j, k])
                
    return L, U

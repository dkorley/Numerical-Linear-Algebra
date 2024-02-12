# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:34:50 2024

@author: dkorley
"""

#linearly independent columns
import numpy as np
def simpleQr(A):
    m, n = A.shape
    R = np.zeros((n, n))
    Q = np.zeros((m, n))
    R[0, 0] = np.linalg.norm(A[:, 0:1])
    Q[:, 0:1] = A[:, 0:1] / R[0, 0]
    
    for k in range(1, n):
        vector_proj = np.zeros((m, 1))
        for i in range(0, k):
            R[i, k] = np.matmul(Q[:, i:i + 1].T, A[:, k:k + 1])
            vector_proj += R[i, k] * Q[:, i:i + 1]
            residual = A[:, k:k + 1] - vector_proj
            
        R[k, k] = np.linalg.norm(residual)
        Q[:, k:k + 1] = residual / R[k , k] 

    return Q, R

# A = np.array([[4., 0, 0, 0], [-4, 8, -4, 2], [-7, 7, -3, 3], [-2, 2, -2, 4]])
# A = np.array([[1., 2, 0], [2, 1, 2], [1, 1, -3]])
A = np.array([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])
Q, R = simpleQr(A)

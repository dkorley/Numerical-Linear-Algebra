# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:08:01 2024

@author: Kali Linux
"""

import numpy as np

#simple QR for linearly dependent matrix columns

def QR(A):
    #dimensions of A
    m, n = A.shape
    
    #initialize Q & R 
    R = np.zeros((n, n))
    Q = np.zeros((m, n))
    
    rank = 0
    
    tolerance = 1e-8
    
    for j in range(0, n):
        vector_proj = np.zeros((m, 1))
        
        for i in range(0, rank):
            vector_proj += R[i, j] * Q[:, i:i + 1]
            
        residual = A[:, j:j + 1] - vector_proj
        norm_residual = np.linalg.norm(residual)
        
        if norm_residual > tolerance:
            rank += 1
            R[rank - 1, j] = norm_residual
            Q[:, rank - 1:rank] = residual / norm_residual
            
            for k in range(j + 1, n):
                R[rank - 1, k] = Q[:, rank - 1:rank].T @ A[:, k:k + 1]
                
    Q = Q[:, 0: rank]
    R = R[0: rank, :]
    
    return Q, R, rank

A = np.array([[4., 0, 0, 0], [-4, 8, -4, 2], [-7, 7, -3, 3], [-2, 2, -2, 4]])
Q, R, rank = QR(A)
                
        
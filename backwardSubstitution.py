# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:10:34 2024

@author: Kali Linux
"""

import numpy as np

def backwardSubstitution(U, z):
    n = U.shape[1]
    
    x = np.zeros((n, 1))
    x[n-1] = z[n-1] / U[n-1, n-1]
    
    for i in range(n - 1, -1, -1):
        totalsum = 0
        for j in range(i + 1, n):
            totalsum += np.dot(U[i, j], x[j])
            
        x[i] = (z[i] - totalsum) / U[i, i]
        
    return x

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:04:02 2024

@author: Kali Linux
"""

import numpy as np

def forwardSubstitution(L, b):
    n = L.shape[1]
    z = np.zeros((n, 1))
    
    z[0] = b[0] / L[0, 0]
    
    for i in range(1, n):
        totalsum = 0
        for j in range(0, i):
            totalsum += np.dot(L[i, j], z[j])
            
        z[i] = (b[i] - totalsum) / L[i, i]
        
    return z

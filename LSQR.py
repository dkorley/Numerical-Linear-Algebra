# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:11:08 2024

@author: Kali Linux
"""
import QRd
import backwardSubstitution as bs
import numpy as np


def LSQR(A, b):
    m, n = A.shape
    Q, R, rank = QRd.QR(A)
    b = np.dot(Q.T, b)
    x = bs.backwardSubstitution(R, b)
    
    return x

A = np.array([[4., 0, 0, 0], [-4, 8, -4, 2], [-7, 7, -3, 3], [-2, 2, -2, 4]])
b = np.array([[1., 2, 3, 4]]).T
x = LSQR(A, b)

print(f"The solution x: \n\n {x}")


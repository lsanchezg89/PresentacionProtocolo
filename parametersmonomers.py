# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:14:42 2016

@author: laura
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

Kc = 0.423


def CalsequestrinM(C):
    CSQ = []
    for k in range(0, n+1):
        CSQC = (mt.factorial(n) * Kc ** (n + k) * C ** (k)) / (
            mt.factorial(n - k) * mt.factorial(k) * (Kc + C) ** n)
        CSQ.append(CSQC)
    CSQ = np.array(CSQ)
    CSQ = np.transpose(CSQ)
    return CSQ

C = np.linspace(0.05, 1.2, 100)

FO = []
for n in range(26, 27):
    CSQ = CalsequestrinM(C)
    Cb1 = []
    for i in range(1, n+1):
        Cb1.append(i * CSQ[:, i])
    Cb1 = np.array(Cb1)
    Cb1 = np.transpose(Cb1)
    Cb = []
    for j in range(0, len(C)):
        Cb.append(sum(Cb1[j, :]) / sum(CSQ[j, :]))
    Cb = np.array(Cb)
    FO.append(Cb)
FO = np.array(FO)
FO = np.transpose(FO)

x = [0.05, 0.15, 0.26, 0.35, 0.53, 0.73, 0.93, 1.18]
y = [1.4, 3.6, 5.5, 7.0, 14.0, 17.0, 19.0, 20.5]

plt.figure()
plt.plot(C, FO)
plt.plot(x, y, '.')
plt.axis([0, 1.2, 0, 30])
plt.show()


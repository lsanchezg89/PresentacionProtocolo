# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:46:05 2016

@author: lsanc_000
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

Kc = 0.1
Kd = 6.0
m = 100


def Calsequestrin(C):
    CSQ = []
    for k in range(0, n+1):
        CSQC = (-(Kc + C) ** n / (mt.factorial(n) / (mt.factorial(
            k) * mt.factorial(n-k)) * Kc ** (n-k) * C ** k) + np.sqrt(((
                Kc + C) ** n / (mt.factorial(n) / (mt.factorial(
                    k) * mt.factorial(n-k)) * Kc ** (
                        n-k) * C ** k)) ** 2 + 4 * (2 / Kd * (C / Kc) ** (
                            2 * (n - k))))) / (2 * (2 / Kd * (C / Kc) ** (
                                2 * (n - k))))
        CSQ.append(CSQC)
    CSQ = np.array(CSQ)
    CSQ = np.transpose(CSQ)
    return CSQ


def Dimers(C):
    return ((4 + Kd * ((Kc + C) / C) ** (2 * n)) - np.sqrt((4 + Kd * ((
            Kc + C) / C) ** (2 * n)) ** 2 - 16))/8

C = np.linspace(0, 1.2, 100)

FO = []
for n in range(12, 13):
    CSQ = Calsequestrin(C)
    DCSQ = Dimers(C)
    Cb1 = []
    for i in range(1, n+1):
        Cb1.append(i * CSQ[:, i])
    Cb1 = np.array(Cb1)
    Cb1 = np.transpose(Cb1)
    Cb = []
    for j in range(0, len(C)):
        Cb.append((sum(Cb1[j, :]) + (2 * n + m) * DCSQ[j]) / (
            sum(CSQ[j, :]) + 2 * DCSQ[j]))
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

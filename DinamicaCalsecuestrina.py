# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:49:54 2016

@author: lsanc_000
"""

import numpy as np
import matplotlib.pyplot as plt

# Los kc son la tasa de reacción de la unión de calcio a calsecuestrina.
# Los kd son la tasa de reacción de la dimerización.


Kc = 0.050335245574337807
Kd = 1.0


def Calsequestrin(C):
    """Calsecuestrina libre"""
    return (-((Kc + C) / Kc) ** 2 + np.sqrt(((Kc + C) / Kc) ** 4 +
            8 * (C ** 4 / (Kc ** 4 * Kd)))) / (4 * (
                C ** 4 / (Kc ** 4 * Kd)))


def CalsequestrinC(C):
    """Calsecuestrina unida a un calcio"""
    return (-(Kc + C) ** 2 / (2 * C * Kc) + np.sqrt((Kc + C) ** 4 /
            (4 * (C * Kc) ** 2) + 2 * C ** 2 / (Kc ** 2 * Kd))) / (
            C ** 2 / (Kc ** 2 * Kd))


def Calsequestrin2C(C):
    """Calsecuestrina unida a dos calcios"""
    return (-(Kc + C) ** 2 / C ** 2 + np.sqrt((Kc + C) ** 4 / C ** 4 +
            8 / Kd)) / (4 / Kd)


def CalsequestrinDimers(C):
    """Dímeros de calsecuestrina"""
    return ((4 + Kd * ((Kc + C) / C) ** 4) - np.sqrt((4 + Kd * (
            (Kc + C) / C) ** 4) ** 2 - 16)) / 8


C = np.linspace(0, 20, 1000)
Q = Calsequestrin(C)
Qc = CalsequestrinC(C)
Qdc = Calsequestrin2C(C)
dQdc = CalsequestrinDimers(C)

plt.plot(C, Q, label='Calsequestrin', color='red')
plt.plot(C, Q, label='Calsecuestrin - Ca', color='purple')
plt.plot(C, Qdc, label='Calsequestrin - 2Ca', color='green')
plt.plot(C, dQdc, label='Calsequestrin Dimers', color='blue')
plt.xlabel(r'$[Ca]$')
plt.ylabel(r'$[\cdot]$')
plt.legend(loc=0)
plt.show()


Cb = np.zeros(1000)
CSQ = np.zeros(1000)
FO = np.zeros(1000)
n = 20
m = 5

for i in range(len(C)):
    Cb[i] = Qc[i] + 2 * Qdc[i] + (n+m) * dQdc[i]
    CSQ[i] = Q[i] + Qc[i] + Qdc[i] + 2 * dQdc[i]
    FO[i] = Cb[i] / CSQ[i]
plt.plot(C, FO)
plt.xlabel(r'$[Ca]$')
plt.ylabel(r'Occ Frec')
plt.legend(loc=0)
plt.axis([0, 25, 0, 80])
plt.show()

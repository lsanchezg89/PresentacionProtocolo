# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:22:05 2016

@author: laura
"""

import numpy as np
import matplotlib.pyplot as plt
from DinamicaCalsecuestrina import Calsequestrin, CalsequestrinC
from DinamicaCalsecuestrina import Calsequestrin2C, CalsequestrinDimers

Kc = 1.0
C = np.linspace(0, 20, 1000)
e = np.linspace(0.01, 100, 10)
Q = Calsequestrin(C)
Qc = CalsequestrinC(C)
Qdc = Calsequestrin2C(C)
dQdc = CalsequestrinDimers(C)

for Kd in e:
    Cb = np.zeros(1000)
    CSQ = np.zeros(1000)
    FO = np.zeros(1000)
    for i in range(len(C)):
        Cb[i] = Qc[i] + 2 * Qdc[i] + 80 * dQdc[i]
        CSQ[i] = Q[i] + Qc[i] + Qdc[i] + 2 * dQdc[i]
        FO[i] = Cb[i] / CSQ[i]
    plt.plot(C, FO)
    plt.xlabel(r'$[Ca]$')
    plt.ylabel(r'Occ Frec')
    plt.hold()

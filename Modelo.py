# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 09:55:59 2016

@author: lsanc_000
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

kf = 4000.
nf = 1.8
beta = 100.
a = 35.0
b = 65.0
c = 1.125e-5
ns = 2.
Ks = 3.0e-7
gamma = 0.052
nv = 1.7
Kr = 1.515e-4
Caibasal = 7.5e-6
CaSRbasal = 1.5e-4
csq = 10.


def Model(X, t):
    KC = (b * gamma ** nv * (Caibasal / beta) ** nf * (CaSRbasal - Caibasal)*(
        ((Caibasal / beta) ** ns + Ks ** ns) / (c * (Caibasal / beta) ** ns))-(
        Caibasal / beta) ** nf) ** (1.0 / nf)

    def Probability(X, t):
        Ind = False
        Condition = (10.0 <= t <= 15.0)
        if Condition:
            Ind = True
        num1 = ((X[0] / beta) * (1. + kf * .02)) ** nf
        P1 = num1 / (KC ** nf + num1) * int(Ind)
        num2 = (X[0] / beta) ** nf
        P2 = num2 / (KC ** nf + num2) * int(not(Ind))
        return P1 + P2
    Cai = X[0] / beta
    Pe = csq * (Kr - CaSRbasal)
    Xi = X[1] + Pe + Kr
    CaSR = 1. / 2 * Xi - 1. / 2 * np.sqrt(Xi ** 2 - 4. * X[1] * Kr)
    J1 = a * (Cai - Caibasal / beta)
    P = Probability(X, t)
    J2 = b * gamma ** (nv) * P * (CaSR - Cai)
    J3 = c * (Cai ** ns) / (Ks ** ns + Cai ** ns)
    xdot = -J1 + J2 - J3
    ydot = (J3 - J2) / gamma
    return np.array([xdot, ydot])

t = np.linspace(0, 30, 1000)
X0 = [7.5e-6, 0.00165]
sol = odeint(Model, X0, t)

X = sol[:, 0]
Y = sol[:, 1]

Cai = X / beta
Pe = csq * (Kr - CaSRbasal)
Xi = Y + Pe + Kr
CaSR = 1. / 2 * Xi - 1. / 2 * np.sqrt(Xi ** 2 - 4 * Y * Kr)

plt.figure()
plt.plot(t, Cai)
plt.figure()
plt.plot(t, CaSR)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:36:10 2021

@author: Samaung
"""

import numpy as np
from scipy.integrate import quad_vec
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

xs=np.arange(0.1,10,0.25)
ys=-1/xs

def f(t, K):
    fn = lambda x: np.exp(-t*x**2)*K
    ma = quad_vec(fn, 1, 10)[0]
    return ma

parametros, erro = curve_fit(f, xs, ys)
xFit = np.arange(0.1, 10, 0.01)
plt.plot(xFit, f(xFit, *parametros))
plt.plot(xs,ys,'o')
plt.show()

print("K =", parametros[0])
print("Mat Cov =", erro)

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 13:06:47 2021

@author: MkCst
"""

"""
TEST de jarque-bera
Concepto: p-value
Objetivo: crear una normal simular Jarque-Bera

Paso 1: Generar un arreglo de numeros aleatorios
Paso 2: visualizar el histograma
Paso 3: ¿Que es jarque-bera?
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2


# Variables
x_size = 10**6
gr_lb = 5000 # Grados de libertad
type_random_var = "normal" #<< normal exponential student chi-squared

if type_random_var == "normal":
    x = np.random.standard_normal(size = x_size) 
    x_str = type_random_var
elif type_random_var == "exponential":
    x = np.random.standard_exponential(size = x_size)
    x_str = type_random_var
elif type_random_var == "student":
    x = np.random.standard_t(df=gr_lb, size=x_size)
    x_str = type_random_var + " (df= "+str(gr_lb) + " )"
elif type_random_var == "chi-squared":
    x = np.random.chisquare(df=gr_lb, size=x_size)
    x_str = type_random_var + " (df= "+str(gr_lb) + " )"

# Computo de "risk metrics"
x_mean = np.mean(x) # media
x_stdev = np.std(x) # desviacion estandar
x_skew =  skew(x) # Asimetria
x_kurt = kurtosis(x) # Curtosis @Doc Leer sobre curtosis en exceso

x_var_95 = np.percentile(x,5) # Valor percentil 95%
x_jb = x_size/6 * (x_skew**2 + 1/4*x_kurt**2)

p_value = 1 - chi2.cdf(x_jb, df=2) # Explicacion: 
"""
    Probabilidad de tener valores a la izquierda 
"""
is_normal = (p_value > 0.05) # equivalente jb < 6

# Impresion de datos 
print(x_str)
print("Media:\t"+str(x_mean))
print("std:\t"+str(x_stdev))
print("skewness:\t"+str(x_skew))
print("Kurtosis:\t"+str(x_kurt))
print("VaR 95%:\t"+str(x_var_95))
print("Jarque-Bera\t"+str(x_jb))
print("P value:\t"+str(p_value))
print("Normal??\t"+str(is_normal))


# Plot histograma
plt.figure()
plt.hist(x, bins=100)
plt.title("Histograma "+ x_str)
plt.show()



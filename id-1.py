# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:20:01 2020

@author: Fran
"""

suma = 0

for x in range(1000):
    if (x%3==0)|(x%5==0):
        suma += x

print("La suma de todos los múltiplos de 3 y 5 entre 0 y 1000 es: ", suma)
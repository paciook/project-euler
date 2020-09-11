# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 02:23:51 2020

@author: Fran
"""

x = 1
ant = 1
suma = 0

while (x < 4e+6):
    suma += x*(x%2==0)
    
    x += ant
    ant = x-ant
    
print("La suma de todos los números de Fibonacci pares"\
      " menores a 4 millones es: ", suma)
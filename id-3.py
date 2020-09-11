# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 02:38:14 2020

@author: Fran
"""

num = 600851475143

x = 2

while (x*x < num):
    if(num%x==0):
        num/=x
        longest = x
    else:
        x+=1
if(num > longest):
    longest = num

print(longest)
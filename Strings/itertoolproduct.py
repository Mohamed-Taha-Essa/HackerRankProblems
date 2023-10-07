# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:05:04 2023

@author: wwwta
"""


from itertools import product 

a= [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c= product(a,b)
print(*c) 
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:27:32 2023

@author: wwwta
"""

from collections import Counter
 
# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print (Counter(myList))
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

# print(Counter(myList).items())
 
# print( Counter(myList).keys())
 
# print( Counter(myList).values())


    
import collections
input()
shoes = collections.Counter(map(int, input().split()))
money = 0
for i in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size]:
        money += price
        shoes[size] -= 1
print(money)


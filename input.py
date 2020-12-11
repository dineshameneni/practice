# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:35:19 2020

@author: Shanthi
"""

x = input()

print(type(x))

y = x.split("\t")
y = [int(x) for x in y]


j = []
for i in range (0,10):
    j.append(input().strip())
    
    
print(j)
    


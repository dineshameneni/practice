# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:59:26 2020

@author: Shanthi
"""

def sum(n):
    for i in range (0,n):
        yield i+i

sum = sum(10)
print(next(sum))


#list compression

v = [[1,2,3],[4,5,6]]
a = [(j*j) for i in v for j in i if j > 2]
print(a)



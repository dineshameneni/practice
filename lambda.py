# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:54:13 2020

@author: Shanthi
"""

def add(a,b):
    c=a+b
    return c
d = add(1,2)
print(d)

e = lambda a,b:0 if a==0 or b==0 else a*b
f = e(2,0)
print(f)


#filter
a = [1,2,3,4,5,6,7]  
b = list(filter((lambda c:c > 3 and c < 5),a))
print(b)


#Map
d = [1,2,3,4,5,6,7] 
e = list(map(lambda x,y :x+y, a,d))
print(e)

#reduce

from functools import reduce
l = [1,2,3,4]
product = reduce(lambda x,y:x*y,l) 
print(product)


# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:46:01 2020

@author: Shanthi
"""

def addition(a,b):
    c = a + b
    return c

addition('10', '10')

addition (a=11,b=9)


addition (b=11,a=9)


def fin(a,b,c,*d):
    print(a,b,c)
    print(d)
    sum = 0
    for i in d:
        sum=sum+i
    print(sum)
        
fin(1,2,3,4,5,6,7,8,8,8)



def addition(*a):
    sum = 0
    for i in a:
        sum=sum+i
    print(sum)

addition(1,2,3,4,5,6,7,8,8,8)


def key1(**a):
    if 'age' in a.keys():
        print(a['age'])
    if 'name' in a.keys():
        print(a['name'])
    
key1(age=30)
    
    
    
    
    
    
    
    
    
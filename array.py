# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:42:38 2020

@author: Shanthi
"""

import array as arr

arr1 = arr.array('i',[1,2,3,4,5,6,7,8,9])
for i in arr1:
    print(i)
print(arr1[2])

arr1.append(11)

arr1.pop()
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:50:59 2020

@author: Shanthi
"""

import numpy as np

a = [1,2,3,4,5,6,78]
b = np.array(a)

c = np.zeros(10)

d = np.ones(10)

print(b)

d = [[1,2,3,4,5],[6,7,8,9,10]]
e = np.array(d)
print(e)

f = [[[1,2,3,4],[4,5,6,7]],[[1,2,3,4],[4,5,6,7]]]
g = np.array(f)
print(g)

print(g.ndim)


h = [[[[1,2,3,4],[4,5,6,7]]],[[[1,2,3,4],[4,5,6,7]]]]
i = np.array(h)
print(i)

print(i.ndim)

j = [1,2,3,4,5,6]
k = np.array(j)

k.reshape(2,3)

k.reshape(1,6)

g[0,0,0]

e[-2,-1]

#slicing 1D

b[1:5]
b[1:5:2]

# data types 

s = ['Apple' , 'cherry' , 'Orange']
t = np.array(s)
print(t)
print(t.dtype)

u = [1,2,3,4,5]
v = np.array(u,dtype = 'S')
print(v)
print(v.dtype)


w = [5.4,6.5,7.6,6.7]
s = np.array(w)
print(s)
s.dtype
x = s.astype('i')
print(x)
print(x.dtype)



#creating a numpy array

y = ([1,2,3])
np.array(y)

z = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(z)

slice_arr = z[1::3]
print(z.ndim)
print(slice_arr)


arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

sliced_arr = arr[:2 , ::3]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)

Index_arr = np.array([[1, 1, 0, 3], 
                 [3, 2, 1, 0]])
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)

print(Index_arr) 

#Basic Array Operations


a1 = np.array([[1, 2],
              [3, 4]])
aa = a1+1
print(aa)

a2 = np.array ([[1,2],
               [3,4]])

aa1 = a1*a2


aa2 = aa1-1

print(aa2.sum())


print(aa2.min())

print(aa2.max())

print(aa2.mean())

print(np.median(aa2))

print(np.std(aa2))

print(aa2.prod())

print(np.var(aa2))

5.67*5.67

#datatype

x1 = np.array([1.0,2.8])
print(x1.dtype)

x2 = np.array([1.6,2.6],dtype = 'i')
print(x2.dtype)

x2.astype('S')

#Math operation with two array


aa3 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.sqrt(aa3))


aa3.T


#n dimensional array

aa3.ndim
aa3.shape
aa3.size
aa3.dtype

#array creation

aa4 = np.full((3,3),6,dtype = 'complex')


#array cretions using array

import array
arr11 = array.array('i',[1,2,3,4,-5])

for i in arr11:
    print(i)



for j  in range(0,len(arr11)):
    print(arr11[j])


#Arrange

arrrr = np.arange(8)
print(arrrr)

a24  = arrrr.reshape(2,4)
print(a24)
print(a24.ndim)   

a42 = a24.reshape(4,2)
print(a42)

a222 = a42.reshape(2,2,2)
print(a222)

a222.ndim
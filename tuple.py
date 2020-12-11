# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:28:59 2020

@author: Shanthi
"""


tuple1 = ()
tuple2 = (1,2,34,34,1,"dinesh")
tuple2.count(34)

for i in tuple2:
    print(i)
    
del tuple1

tuple3 = (1,2,3,"dinu0",334)
tuple4 = tuple2+tuple3


#set

set1 = (1,2,3,4,5,11,1,2,3,5)
set1 = set(set1)

set1.add()
set1.add(7)
set1.add((6,7))
set1.update([10, 11])


for i in set1:
    if type(i)!=int:
        for j in i:
            print(j)
    else:
        print(i)
        
set1.discard(6)
set1.pop()

set1.clear()

frozen = frozenset(set1)

frozen.pop()


set2 = set((1,2,3,4))
set3 = set1.intersection(set2)
set4 = set1.union(set2)
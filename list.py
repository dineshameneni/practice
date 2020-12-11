# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:59:11 2020

@author: Shanthi
"""

arraylist = ['string','jkjn','1111','12344',222344,'@@#$']
print(len(arraylist))
for i in arraylist:
    print(i)
    
arraylist.append("123455")

arraylist.append(7455558)

arraylist1 = arraylist
arraylist1.append(12456789098765)
arraylist2 = arraylist.copy()
arraylist2.append(745630147896)

arraylist.pop(2)

arraylist.remove("jkjn")

arraylist.insert(1, "85222258")


emptylist = []
for i in range (0,10):
    emptylist.append(i)
for i in range (0,1):
    emptylist.pop(i)

for i in emptylist:
    emptylist.remove(i)
    
emptylist.append(12223)

emptylist[0] = 12345

print(emptylist.reverse())
print(emptylist.sort(reverse=True))
print(emptylist[-2:])


def checkList(hello):
    hello.append(1)
    print(hello)

hello =[]
checkList(hello)


string = "abc"

abc, bca, cab, acb,cba


for i in string:
    for j in string:
        for k in string:
            if i==j or j==k or i==k:
                pass
            else:
                print(i,j,k)


d = ["ABC","Bac","CAB","Bat","tab","Ban"]
dict_ ={}
list_=[]
for i,j in enumerate(d):
    d[i] = j.lower()
    string = "".join(sorted(d[i]))
    print(string)
    list_=[]
    if string in dict_.keys():
        list_ = dict_[string]
        list_.append(j)
        dict_[string]= list_
    else:
        list_.append(j)
        dict_[string]=list_

print(dict_)

for key, value in dict_.items():
    print(value)
    
    
    li = [1,2,4,2,5,3,2,6,8,9,5]


dict_ = {"eno" : 1, "name": "a", "Age":21}

for k,v in dict_.items():
    print(k,v)
    
print(dict_["name"])    
print(dict_.values())
print(dict_.keys()) 

dict_["dept"]="chemistry"
dict_["dept"]="physics"
dict_.pop("dept")

for k,v in sorted(dict_.items()):
    print(k,v)
    

import operator
li = [1,2,4,2,5,3,2,6,8,9,5]
dict1={}
for i in li:
    if i in dict1.keys():
        dict1[i] = dict1[i]+1
    else:
        dict1[i]=1
print(dict1)
for k,v in sorted(dict1.items(),key=operator.itemgetter(1) ,reverse = True):  
    print(k,v)          
        
   
        
        
    
    
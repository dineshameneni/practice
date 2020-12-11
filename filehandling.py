# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:48:27 2020

@author: Shanthi
"""

import os

print(os.getcwd())

path = os.path.join(os.getcwd(),"Desktop\Practise\practice")

for file in os.listdir(path):
    if file.endswith('.txt'):
        f = open(os.path.join(path,'demo.txt'),'r')
        s = f.read()
        print(s)
        f.close()
    else:
        print('file does not exist')
        
        
f = open(os.path.join(path,'demo.txt'),'a')
#s = f.read()
print(s)
f.write("\n please stop hi hr u wru \n")
f.close()


with open(os.path.join(path,'demo1.txt'),'a') as newfile:
    newfile.write("\n hello")
    
    
for root, dir_, file in os.walk(".",topdown = False,):
    for f in file:
        if f== 'demo.txt':
            print("file exist")
            break
        
      
os.makedirs('demo3')

os.removedirs("demo3")

if os.path.exists((os.path.join(path,'demo2.txt'))):
    print("exist")
    

for file in os.listdir(path):
    if file.startswith('demo'):
        """f = open(os.path.join(path,'demo.txt'),'r')
        s = f.read()
        print(s)
        f.close()"""
        print(file)
    else:
        print('file does not exist')
        

newpath = os.path.split(path)
newpath = newpath[0]
newpath = os.path.split(newpath)
newpath = newpath[0]
newpath = os.path.join(path,'demo.txt')
os.path.basename(newpath)


with open(os.path.join(path,'demo.txt'), 'r') as access:
    for line in access.readlines():
        for l in line.split():
            print(l)
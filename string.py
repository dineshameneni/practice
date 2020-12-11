# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:36:50 2020

@author: Shanthi
"""

i=10
j=10

name = "dinesh"
print(name[::-1])
print(name[9:9])

for i in name:
    print(i)
    
for i in range (0,len(name)):
    print(name[i])
    
description = """This specially designed Python tutorial will help you learn Python 
Programming Language in most efficient way, with the topics from basics to advanced 
(like Web-scraping, Django, Deep-Learning, etc.) with examples.
"""
print(description.lower())

del description
print(description)

firstname = "dinesh"
lastname = "ameneni"
print(firstname+" "+lastname)
previousname = lastname
lastname = "ytyhhyhnuun"
print(lastname)
print(previousname)
print(firstname+" "+lastname)


print("my first name {1},my last name {0}".format(firstname, previousname))

description = """This specially designed Python tutorial will help you learn Python 
Programming Language in most efficient way, with the topics from basics to advanced 
(like Web-scraping, Django, Deep-Learning, etc.) with examples.
"""
print(description.split(','))
count = description.split(',')
print(len(count))

for i,j in enumerate(count):
    print(i,j)


a, b, c, d, e ='a','b','c','d','e'
print(a, b, c, d, e)
a, b, c, d, e = e,d,c,b,a
print(a, b, c, d, e)

num = "123asdf$%&**$$4"
if(num.isdigit()):
    print("ir is num")
else:
    if(num.isalnum()):
        print("it is a alphanumeric")
    else:
        if(num.isalpha()):
            print("it is alpha")
        else:
            print("it is not alphanumeric")

num1 = " ddddd  "
num2 = num1.strip()
print(num2)



def palindrome(n):
    r = n[::-1]
    print(r)
    print(n)
    if(r==n):
        print("it is palindrome")
    else:
        print("it is not palindrome")
n = "liriljj"
palindrome(n)


def palin(n):
    reverse = ""
    #j = 0
    for i in range(1,len(n)+1):
        #j=j+1
        print(i)
        #reverse = reverse + n[1-len(n)]
        reverse = reverse + n[-i]
    print(reverse)
    if(reverse==n):
        print("it is palindrome")
    else:
        print("it is not palindrome")

palin("malayalam")

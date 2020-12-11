# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:24:50 2020

@author: Shanthi
"""



#start
x=10
if(x>15):    
    print("10 is greater than 15")
else:
    print("10 is less")
#end
teamplayers = 11
ball = 1
bat = 2
umpire = 3
weather = "sunny"
def checkPlayingcondition(teamplayers,ball,bat,umpire,weather):
    if teamplayers >= 11:
        if (ball >= 1) and (bat >= 2):
            #if bat >= 2:
            if umpire >= 3:
                if (weather == "sunny") or (weather == "bad light"):
                
                    print ("yes we can cricket")
                else:
                    print("weather should be sunny")
            else:
                print("three umpires are required")
            #else:
                #print("Two bat are required")
        else:
            print(" one ball required to play")

    else:
        print("Team size should be 11")

checkPlayingcondition(11,2,1,3,"bad light")

def printnums(n):
    for i in range (0,n+1,5):
        print(i)

printnums(10)

import random
def superover(overs):
    totalruns = 0
    for over in range(1,overs+1):
        runsperover = 0
        balls = 1      
                
        while(balls <= 6):
            runs = random.randint(0, 6)
            print("over :" + str(over) +" Ball :"+str(balls)+" Runs :"+str(runs))
            runsperover = runsperover + runs
            balls = balls+1
        print("this over concedes runs"+str(runsperover))
        totalruns = totalruns + runsperover        
    print("total  runs: " +str(totalruns))   
superover(2)

multi = 1
nums = 1
while(nums <= 10):
    multi = nums*multi
    nums = nums+1  
print("multi of 10: "+str(multi))

def factorial(n):
    
        
        if(n==1):
            return 1
        else:
            return n * factorial(n-1)
for n in range(1,10):
    fact = factorial(n)
    print("factorial of "+str(n)+": "+str(fact))



def fabonninc(n):
    if(n<=2):
        return 1
    else:
        return fabonninc(n-1) + fabonninc(n-2)
    
for n in range (1,10):
    fab = fabonninc(n)
    print("fabonnic of "+str(n)+":"+str(fab))
    
    
def odd(n):
    if(n%2 ==0):
        print("the number is even:" +str(n))
    else:
        pass
for n in range (1,10):
    odd(n)
        
    
def speedlimit(speed):
    if(speed>=80):
        print("ticket is generated: " +str(speed))
    else:
        print("no ticket")
        
speedlimit(80)
        
for i in range (1,10):
    if(i == 7):
        break
    print(i)   
    
num=0    
while (num<=10):
    print(num)
    num=num+1
    
num=1
while(num<=5):
    print()
    
def vit(n):
    k=2*n-2
    for i in range(0,n):
        for j in range (0,k):
            print(end=" ")
        k= k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
vit(5)
    
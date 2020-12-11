# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:26:11 2020

@author: Shanthi
"""

class Banking():
    crtbal = 0
    bankname= " "
    def __init__(self,crtbal,bankname):
        self.crtbal = crtbal
        self.bankname = bankname
    def deposit(self,depamt):
        self.crtbal = self.crtbal+depamt
        return self.crtbal
    
    def withdraw(self,withdrawamt):
        if self.crtbal >= withdrawamt:
            self.crtbal = self.crtbal - withdrawamt
        else:
            print("Withdraw amount exceeds current balance")
    
    def checkbal(self):
        print("your account balance is : " +str(self.crtbal))

    def checkbank(self):
        print("ur bank name : " +self.bankname)
ba = Banking(100, "SBI")
ba.checkbal()  
ba.checkbank()
ba.withdraw(50) 

ba1 = Banking(200, "ICICI") 
ba1.checkbal()
ba1.checkbank()  
    
        
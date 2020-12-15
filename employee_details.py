# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:26:23 2020

@author: Shanthi
"""

import utility as g
import datetime
import pyodbc

class Employee:
    def addemployee(self,firstname,lastname,salary,deptid,managerid,addressid,designationid,professionalid,branchid,personalid,contactid):
        connection = g.sqlServerConnection()
        cursor = connection.cursor()
        
        cursor.execute('select isnull(max(empid),0)+1 as employee from employee')
        empid = cursor.fetchone()
        
        cursor.execute('select User_name(1)')
        username = cursor.fetchone()
        
        cursor.execute("select getdate()")
        get_date = cursor.fetchone()
        
        if firstname is not None or lastname is not None or salary > 0 or deptid > 0 or managerid > 0 or addressid > 0 or designationid > 0 or professionalid > 0 or branchid > 0 or personalid > 0 or contactid > 0:
            try:
        
                cursor.execute('insert into employee values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',\
                               empid[0],firstname,lastname,salary,deptid,managerid,addressid,designationid,\
                                   professionalid,branchid,personalid,contactid,username[0],get_date[0],username[0],get_date[0])
                connection.commit()
            except pyodbc.Error as e:
                print("there is error in db:"+str(e))
        else:
            print("invalid data")
        cursor.close()
        del cursor
        
        g.sqlServerDisconnect(connection)
        
emp = Employee()
emp.addemployee(firstname='Dinesh', lastname = 'A', salary = 10000, deptid = 1, managerid = 1, addressid =1, designationid = 1, professionalid =1, branchid =1, personalid =1, contactid =1)
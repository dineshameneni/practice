# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:07:34 2020

@author: Shanthi
"""

import utility as util
#from utility import Connections

import os
import pandas as pd

print(os.getcwd())

class Employee():
    def addEmployee(self,fname,lname,deptid):
        connect = util.sqlServerConnection()
        cursor = connect.cursor()
        cursor.execute('select ISNULL(max(empid),0)+1 as empid from employee;')
        empid = cursor.fetchone()
        
      #  insertCursor = connect.cursor()
        cursor.execute("insert into employee values(?,?,?,?)",empid[0],fname,lname,deptid)
        connect.commit()
        
        print("emp added in db")
        cursor.close()
        del cursor
        """insertCursor.close()
        del insertCursor"""
        util.sqlServerDisconnect(connect)
        
    def deleteEmployee(self, empid):
        connect = util.sqlServerConnection()
        deleteemp = connect.cursor()
        deleteemp.execute('delete from employee where empid = ?',empid)
        connect.commit()
        
        print('employee is deleted')
        
        deleteemp.close()
        del deleteemp
        
        
        
    def updateEmployee(self, empid,lname,deptid):
        connect = util.sqlServerConnection()
        updateemp = connect.cursor()
        
        if lname is not None and deptid is not None:
            try:
                updateemp.execute('update employee set lname = ?,deptid = ? where empid = ?',lname,deptid,empid)
            except:
                print("please check the sql query")
            print("lname , deptid is updated")
        
        else:
            if lname is None:
                if deptid is not None:
                    updateemp.execute('update employee set deptid = ? where empid = ?',deptid,empid)
                
                    print("depid is updated")
            else:
                updateemp.execute('update employee set lname = ? where empid = ?',lname,empid)
            
                print("lname is updated")
        
        connect.commit()
        updateemp.close()
        del updateemp
        
        
    def employeeReport(self, filetype):
        connect = util.sqlServerConnection()
        #empRpt = connect.cursor()
        
        #emprRpt.execute('select * from employee')
        query = "select * from employee;"
        data = pd.read_sql(query,connect)
        if filetype == '.csv':
            data.to_csv(os.path.join(os.getcwd(),'red.csv'),index = False)
        elif filetype == '.xlsx':
            data.to_excel(os.path.join(os.getcwd(),'rs.xlsx'),index = False)
        else:
            data.to_json(os.path.join(os.getcwd(),'rsee.json'))
        print("report is ready")
        
        util.sqlServerDisconnect(connect)
        
        
emp = Employee()

emp.employeeReport(filetype = '.csv')






emp.updateEmployee(4, 'a', 4)

emp.updateEmployee(empid = 2,lname = 'ffff', deptid= 7)
emp.deleteEmployee(3)


#emp.addEmployee('Dinesh', 'Ameneni', 1)

emp.addEmployee('shanthi', 'Ameneni', 2)

emp.addEmployee('satish', 'korapati', 4)



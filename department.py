# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:04:33 2020

@author: Shanthi
"""

import utility as utt
import datetime
import pyodbc

class Department():
    def adddepartment(self,dep_Description,dep_status = None):
        connection = utt.sqlServerConnection()
        cursor = connection.cursor()
        cursor.execute('Select ISNULL(MAX(Deptid),0)+1 as department from department')
        
        Deptid = cursor.fetchone()
        cursor.execute('SELECT USER_NAME(1)')
        username = cursor.fetchone()
        
        cursor.execute('select GETDATE()')
        get_date = cursor.fetchone()
        
        
        if dep_status is None:
            try:
                
                cursor.execute('''insert into department(Deptid,dep_Description,created_by,created_datetime,
                           modified_by, modified_datetime) 
                values(?,?,?,?,?,?)''',Deptid[0],dep_Description,username[0],get_date[0],username[0],get_date[0])
            except pyodbc.Error as ex:
                print("There is some db error" +str(ex))
                connection.rollback()
            finally:
                print("please check the data while inserting")
        else:
            try:
                cursor.execute('''insert into department(Deptid,dep_Description,dept_status,created_by,created_datetime,
                           modified_by, modified_datetime) 
                values(?,?,?,?,?,?,?)''',Deptid[0],dep_Description,dep_status,username[0],get_date[0],username[0],get_date[0])
            
            except pyodbc.Error as ex:
                print("There is some db error" +str(ex))
                connection.rollback()
            finally:
                print("please check the data while inserting")
            
        connection.commit()
               
        cursor.close()
        del cursor
        
        utt.sqlServerDisconnect(connection)
        
        
department = Department()
department.adddepartment('finanace department', 'Y')
        
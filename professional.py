# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:31:02 2020

@author: Shanthi
"""

import utility as ut
import datetime
import pyodbc

class Profession():
    def addprofession(self,Doj,dor,designation,companyname,proffession_Address,salary):
        connection = ut.sqlServerConnection()
        cursor = connection.cursor()
        cursor.execute('Select isnull(max(professionalid),0)+1 as professional from professional')

        professionalid = cursor.fetchone()
            
        cursor.execute('SELECT USER_NAME(1)')
        username = cursor.fetchone()
        
        cursor.execute('select GETDATE()')
        get_date = cursor.fetchone()
        
        
        if salary > 0 and companyname is not None and len(companyname) > 0 and \
        Doj is not None and dor is not None and designation is not None and \
            proffession_Address is not None:
            try:
                cursor.execute('insert into professional values (?,?,?,?,?,?,?,?,?,?,?)',\
                               professionalid[0],Doj,dor,designation,companyname,proffession_Address,\
                                   salary,username[0],get_date[0],username[0],get_date[0])
                connection.commit()
            except pyodbc.Error as e:
                print('there is error in db'+str(e))
                connection.rollback()
            
            finally:
                print("please insert the data correctly")
                
                
        else:
            print("invalid data")
        
        cursor.close()
        del cursor
        

profession = Profession()
profession.addprofession('2020-12-22','2020-12-31', 'software', 'Ruptub','bommanhalli',10000)
        
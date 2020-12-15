# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:25:43 2020

@author: Shanthi
"""

import utility as f
import datetime
import pyodbc

class Personal():
    def addpersonal(self,firstname,lastname,dob,maritalstatus,aadharid,voterid,pancardno,gender,professionalid\
                    ,passportno,passportvalid,addressid):
        connection = f.sqlServerConnection()
        cursor = connection.cursor()
        
        cursor.execute('Select isnull(max(personalid),0)+1 as personal from personal')
        personalid = cursor.fetchone()
        
        cursor.execute('select user_name(1)')
        username = cursor.fetchone()
        
        cursor.execute('select getdate()')
        get_date = cursor.fetchone()
        
        if firstname is not None or lastname is not None or dob is not None or maritalstatus is not None or aadharid is not None or voterid is not None or pancardno is not None\
            or gender is not None or professionalid is not None or passportno is not None or passportvalid is not None or addressid is not None:
            
            try:
                cursor.execute('insert into personal values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',personalid[0],\
                               firstname,lastname,dob,maritalstatus,aadharid,voterid,pancardno,gender,\
                                   professionalid,passportno,passportvalid,addressid,username[0],get_date[0],\
                                       username[0],get_date[0])
                connection.commit()
                
            except pyodbc.Error as e:
                print("there error in db"+str(e))
                connection.rollback()
        else:
             print('invalid data')
             
             
        cursor.close()
        del cursor
        
        f.sqlServerDisconnect(connection)
        
        
personal = Personal()
personal.addpersonal('shanthi','A','1990-10-22','Married',2010102010201234,'BK345678','AB3456789','Female',2,'AMN34567890','2035-10-22',2)

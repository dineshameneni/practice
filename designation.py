# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:43:54 2020

@author: Shanthi
"""

import utility as d
import datetime
import pyodbc

class Designation():
    def adddesignation(self,designation_description,designation_status,Branchid):
        connection = d.sqlServerConnection()
        cursor = connection.cursor()
        
        cursor.execute('Select isnull(max(designationid),0)+1 as designation from designation')
        designationid = cursor.fetchone()
        
        cursor.execute('select user_name(1)')
        username = cursor.fetchone()
        
        cursor.execute('select getdate()')
        get_date = cursor.fetchone()
        
        if (designation_description is not None and len(designation_description.strip()) > 0) \
            or designation_status is not None or Branchid is not None:
            try: 
                cursor.execute('insert into designation values(?,?,?,?,?,?,?,?)',designationid[0],\
                               designation_description,designation_status,Branchid,username[0],get_date[0],\
                                   username[0],get_date[0])
                connection.commit()
            
            except pyodbc.Error as e:
                print("there is error in db"+str(e))
                connection.rollback()
            
        else:
            print('invalid data')
        cursor.close()
        del cursor
        
        d.sqlServerDisconnect(connection)
        

designation = Designation()
designation.adddesignation('Tech support','Y',3)
        
        
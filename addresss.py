# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:17:19 2020

@author: Shanthi
"""

import utility as utill
import datetime
import pyodbc

class Address():
    def addaddress(self,type_of_address,addline1,addline2,Landmark,District,state_,country,Pincode,add_status):
        connection = utill.sqlServerConnection()
        cursor = connection.cursor()
        cursor.execute('Select isnull(max(addressid),0)+1 as address from addresss ')
        
        addressid = cursor.fetchone()
        
        
        cursor.execute('SELECT USER_NAME(1)')
        username = cursor.fetchone()
        
        cursor.execute('select GETDATE()')
        get_date = cursor.fetchone()
        
        if (type_of_address == 'Permanent' or type_of_address =='Current') and (len(addline1.strip()) > 0 and addline1 is not None) \
            and addline2 is not None and \
        country == 'India' and Landmark is not None and District is not None and (Pincode is not None and len(str(Pincode))== 6):
            try:
                cursor.execute('insert into addresss values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',\
                               addressid[0],type_of_address,addline1,addline2,Landmark,District,state_,\
                                   country,Pincode,add_status,username[0],get_date[0],username[0],\
                                   get_date[0])
                connection.commit()
                
            except pyodbc.Error as e:
                print('there is error in db'+str(e))
                connection.rollback()
            
                
        else:
            print('Invalid Data')
                
                
        cursor.close()
        del cursor
               
        utill.sqlServerDisconnect(connection)


address = Address()
address.addaddress('Current','kormanagal','8th block', 'Near Mangal mantapa', 'Bangalore', "Karnataka", 'India', 560065, 'N')
        
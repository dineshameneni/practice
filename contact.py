# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:00:21 2020

@author: Shanthi
"""

import utility as ut
import datetime

class Contact():
    def addContact(self,emailid,phoneno,alternatephoneno):
        connection = ut.sqlServerConnection()
        cursor = connection.cursor()
        cursor.execute('Select ISNULL(MAX(contactid),0)+1 as contact from contact')
        
        
        contactid = cursor.fetchone()
        cursor.execute('SELECT USER_NAME(1)')
        username = cursor.fetchone()
        
        cursor.execute('select GETDATE()')
        get_date = cursor.fetchone()
        
        if phoneno is not None and phoneno > 0 and \
            len(str(phoneno)) == 10 and type(phoneno) == int:
                if alternatephoneno is not None and alternatephoneno > 0 and \
                    len(str(alternatephoneno)) == 10 and type(alternatephoneno) == int:                
                        cursor.execute('insert into contact values(?,?,?,?,?,?,?,?)',contactid[0],emailid,phoneno,alternatephoneno
                       ,username[0],get_date[0],username[0],get_date[0])
                        connection.commit()
                else:
                    print("alternate num is not valid")
        else:
            print("phone no is not valid")
        
        
        cursor.close()
        del cursor
    
contact = Contact()
contact.addContact('bca@gmail.com', 9739999999, 9999899999)
        
        
        
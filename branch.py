# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:56:37 2020

@author: Shanthi
"""

import utility as utilll
import datetime
import pyodbc

class Branch():
    def addbranch(self,branch_desc,addressid,branch_status):
        connection = utilll.sqlServerConnection()
        cursor = connection.cursor()
        
        cursor.execute('select isnull(max(Branchid),0)+1 as branch from branch')
        
        Branchid = cursor.fetchone()
        
        cursor.execute('select user_name(1)')
        username = cursor.fetchone()
        
        cursor.execute('select getdate()')
        getdate = cursor.fetchone()
        
        if (branch_desc is not None and len(branch_desc.strip()) > 0) or addressid is not None or \
            branch_status is not None:
                try:
                    
                    cursor.execute('insert into branch values (?,?,?,?,?,?,?,?)',Branchid[0],\
                                   branch_desc,addressid,branch_status,username[0],getdate[0],username[0],getdate[0])
                    connection.commit()
                
                except pyodbc.Error as e:
                    print('there is error in db'+str(e))
                    connection.rollback()
        else:
            print('invalid data')
        cursor.close()
        del cursor
        
        utilll.sqlServerDisconnect(connection)
        
branch = Branch()
branch.addbranch('Btm Layout',2,'Y')
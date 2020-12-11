# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:10:42 2020

@author: Shanthi
"""

import pyodbc

#class Connections():

def sqlServerConnection():
    server = 'DESKTOP-LFUN2G8' 
    database = 'sample1'
    connection = pyodbc.connect('Trusted_Connection=yes',
               driver='{SQL Server}', server=server,
               database=database)
    return connection

def sqlServerDisconnect(connection):
    connection.close()
    
    
"""
cursor = connection.cursor()

print(cursor)


print(connection)

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()
"""
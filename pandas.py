# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:13:33 2020

@author: Shanthi
"""

#Desktop\Practise\practice

import pandas as pd 
import os
import matplotlib.pyplot as plt
import seaborn as sb
print(os.getcwd())
path = os.path.join(os.getcwd(), "Desktop\Practise\practice")
print(path)
path = os.path.join(path, "Dataset3.csv")
print(path)

data = pd.read_csv(path,sep=";")

print(data.columns)


data.info()

data.describe()

data.head(10)

data.tail(10)

data1 = data[['No','Country']]

data2 = data1.loc[data1.Country == "Austria"]

data3 = data.loc[data.Country == "Austria"]

data4 = data.loc[(data["Level of development"] == "Developed") & (data["European Union Membership"] == "Member")] 

data5 = data.groupby("Level of development") ["Country" ,"European Union Membership"]


data5 = data.groupby("Level of development").count() [["Country" , "European Union Membership"]]

data5.boxplot()

data5.plot.bar()

data6 = data[['Inflation rate']]
data7 = data['Entrepreneurship Index']

data6.hist()

plt.scatter(data6, data7)
plt.show()

data8 = data[['Inflation rate' , 'Entrepreneurship Index']]

data8.corr()


data.rename(columns = {"European Union Membership":"Membership"},inplace = True)


data.rename(columns = {"Level of development":"lod"},inplace = True)

data["new"] = data['Inflation rate'] + data['Entrepreneurship Index']
data['new1'] =0

data.drop(columns=['new1'],inplace=True)

pathSave = os.path.join(os.getcwd(), "Desktop\Practise\practice")
print(pathSave)

pathSave = os.path.join(pathSave,'Transformed.csv')
data.to_csv(path_or_buf = pathSave)

data12 = data.select_dtypes(exclude = ['float64','int64'])

data13 = data12['Level of development'].apply(lambda x : x.upper())

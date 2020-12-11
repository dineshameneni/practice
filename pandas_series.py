# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:13:13 2020

@author: Shanthi
"""

import pandas as pd
import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10])
series = pd.Series(data)

print(series)



data1 = np.array([1,2,3,4,5,6,7,8,9,10])
series1 = pd.Series(data1,index = [4,5,6,7,8,9,10,11,12,13])
print(series1[7])

import os
path = os.path.join(os.getcwd(),'Desktop\Practise\practice')
filepath = os.path.join(path,'Dataset3.csv')
print(filepath)
data2 = pd.read_csv(filepath, sep=";")
data2.columns

series2 = data2['Country']

print(series2[5])

print(series2[:9])

print(series2.head())

print(series2.tail())

print(series2.info())

print(series2.describe())

print(series2.loc[series2['Country'] == 'Germany'])
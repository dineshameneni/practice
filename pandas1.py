# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:45:49 2020

@author: Shanthi
"""

import pandas as pd

import os

print(os.getcwd())

#BR_category_id.json

path = os.path.join(os.getcwd(), "Desktop\Practise\practice")
print(path)
filePath = os.path.join(path, "BR_youtube_trending_data.csv")
print(filePath)


data21 = pd.read_csv(filePath)

print(data21.columns)

print(data21.shape)


data22 = data21.loc[:11500,:]
data23 = data21.loc[11501:,:]

data24 = pd.concat([data22,data23])

data22.head()

data22.columns

data25 = data22[['video_id', 'title','description']]

data25.head()



import re
def removespecialchars(text):
    #removespecial = re.compile('^[A-Za-z0-9 ]')
    text = re.sub(r'[^A-Za-z0-9 ]',' ',text)
    return text

data25['description'] = data25['description'].apply(lambda x: removespecialchars(str(x)) )  

print(re.sub(r'[^A-Za-z0-9 ]',' ','ITZY Not Shy M/V[ITZY Official] https://www.youtube.com/c/ITZYhttps://www.instagram.com/itzy.all.in.us/http://www.twitter.com/ITZYOfficialhttp://www.facebook.com/OfficialITZYhttp://ITZY.jype.comhttp://fans.jype.com/ITZY#ITZY #NotShy #ITZY_NotShyCopyrights 2020 ⓒ JYP Entertainment. All Rights Reserved'))


text = 'ITZY Not Shy M/V[ITZY Official] https://www.youtube.com/c/ITZYhttps://www.instagram.com/itzy.all.in.us/http://www.twitter.com/ITZYOfficialhttp://www.facebook.com/OfficialITZYhttp://ITZY.jype.comhttp://fans.jype.com/ITZY#ITZY #NotShy #ITZY_NotShyCopyrights 2020 ⓒ JYP Entertainment. All Rights Reserved'
print(removespecialchars(text))

data25.head()
data25.info()

y = data21.dtypes

jsondata = pd.read_json(os.path.join(os.getcwd(),'rsee.json'))


exceldata = pd.read_excel(os.path.join(os.getcwd(),'rs.xlsx'))

txtdt = pd.read_csv(os.path.join(os.getcwd(), 'empdata.txt'), sep=",", index_col=(None))










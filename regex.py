# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:51:31 2020

@author: Shanthi
"""

import re

var = "dinesh, ZAN ddhdh, dhdhdhdh, din#@$$@@#$$esh 8050567301 yyfkfkf 20 Nov 20205664"
y = re.search("dinesh",var)
print(y)

x=re.findall("dinesh", var)

z = re.compile('[a-z]')
print(re.sub('[^a-zA-Z @]','', var))


print(re.sub('[^0-9 ]','', var))



closingDate = re.findall('[0-9]{2}[ ]+[A-Za-z]{3}[ ]+[0-9]{4}',var)

print(closingDate)

print(re.sub(r'^\d{2} \w{3} \d{4}','',var))
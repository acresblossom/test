# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:29:32 2019

@author: ASUS
"""

import json
fn="restaurant_C_f.json"
with open(fn,'r',encoding='UTF-8-sig',) as fnObj:
    data=json.load(fnObj)

print(data)
print(type(data))

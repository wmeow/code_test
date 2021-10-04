#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:23:18 2021

@author: weimiao
"""

from pymongo import MongoClient
import json
import pymongo
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient("mongodb+srv://test1:123123abcabc@cluster0.40qug.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client.admin

# query 
table = client.test.users

pipeline = table.find(
    {"houses.neighborhood": "Uptown"}, 
    {"houses": {"$elemMatch": {"neighborhood": "Uptown"}}})
res = []
for i in pipeline:
    res.append(i)
print(res)
client.close()

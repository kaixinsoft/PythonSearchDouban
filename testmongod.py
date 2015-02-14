#!/usr/bin/python
#-*-coding:utf-8-*-

from pymongo import MongoClient
import datetime

client = MongoClient()

db = client.test_database

post = {
        "author": "aho",
        "text" : "my first blog post!",
        "tags":["mongo","python","pymongo"],
        "date":datetime.datetime.utcnow()
        }
posts = db.posts
posts.insert(post)

re = posts.find_one()
print re

for re in posts.find():
    print re

# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, jsonify, make_response
from functools import wraps
import pymongo

# 初始化flask应用
app = Flask(__name__)

# 建立连接
client = pymongo.MongoClient(host='localhost',port=27017)
# 得到数据库
db = client.mtodo
# 得到数据集合
lists = db.lists

# 数据库结构样例
# list = {
#     "title": "阅读清单",
#     "created_time": datetime.now(),
#     "todolist": [
#         {
#             "title": "买东阿阿胶",
#             "completed": "False",
#             "isdelete": "False",
#             "created_time": datetime.now()
#         }
#     ]
# }

a = lists.find({'title':'电影清单'})
b = []
for x in a:
    b.append({'_id':x['_id'],'title':x['title']})
b
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

# 跨域访问装饰器
def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

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


# 检索清单
@app.route('/', methods=['GET'])
@allow_cross_domain
def get_lists():
    relist = []
    for x in lists.find():
        relist.append({'_id':str(x['_id']),'title':x['title']})
    return jsonify(relist)

# 检索任务
# @app.route('/id', methods=['GET'])
# def get_todos():
#     list = lists.find_one()
#     return jsonify(list['todolist'])

# 新建清单
# @app.route('/', methods=['POST'])
# def add_list():
#     lists.insert_one({'title':"温泉清单"})
#     return "成功新建清单"

# 更新任务
# @app.route('/', methods=['PUT'])
# def update_todo():
#     lists.update({'title':"阅读清单"},{"$push":{'todolist':{'title':"你你你你...."}}})
#     return "成功新建任务"

# 删除任务

if __name__ == '__main__':
    app.run(debug=True)

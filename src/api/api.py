# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, jsonify, make_response ,request
from functools import wraps
import pymongo
from bson.objectid import ObjectId

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

# 数据库结构
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

# 新增清单
@app.route('/add', methods=['POST'])
@allow_cross_domain
def add_list():
    title = request.values.get('title')
    lists.insert_one({'title': title, "created_time": datetime.now(), "todolist":[]})
    relist = []
    for x in lists.find():
        relist.append({'_id':str(x['_id']),'title':x['title']})
    return jsonify(relist)

# 删除清单
@app.route('/delete', methods=['POST'])
def del_list():
    listId = request.values.get('listId')
    lists.remove({'_id':ObjectId(listId)})
    return jsonify('删除成功')

# 修改清单
@app.route('/update', methods=['POST'])
def upd_list():
    listId = request.values.get('listId')
    title = request.values.get('title')
    lists.update({'_id':ObjectId(listId)},{"$set":{"title":title}})
    return jsonify('修改成功')

# 检索任务
@app.route('/todos', methods=['POST'])
@allow_cross_domain
def get_todos():
    listId = request.values.get('listId')
    retodos = lists.find_one({'_id':ObjectId(listId)})['todolist']
    return jsonify(retodos)

# 新增任务
@app.route('/todos/add', methods=['POST'])
@allow_cross_domain
def add_todos():
    listId = request.values.get('listId')
    todoTitle = request.values.get('todoTitle')
    todolist = lists.find_one({'_id':ObjectId(listId)})['todolist']
    todolist.append({"title":todoTitle, "completed": "False", "isdelete": "False", "created_time": datetime.now()})
    lists.update({'_id':ObjectId(listId)},{"$set":{"todolist":todolist}})
    return jsonify('新增任务成功')

# 删除任务
@app.route('/todos/delete', methods=['POST'])
@allow_cross_domain
def del_todos():
    listId = request.values.get('listId')
    item = request.values.get('item')
    todolist = lists.find_one({'_id':ObjectId(listId)})['todolist']
    index = todolist.indexOf(item)
    todolist.splice(index, 1)
    lists.update({'_id':ObjectId(listId)},{"$set":{"todolist":todolist}})
    return jsonify('删除任务成功')


# 更新任务



if __name__ == '__main__':
    app.run(debug=True)

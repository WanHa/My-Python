#!/usr/bin/python3
 
import pymysql
import uuid

#namea=input('please enter your name: ')
# 打开数据库连接
db=pymysql.connect(host='127.0.0.1',port=3306,user='wh',password='123456',db='test', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * from test.node_user")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
if cursor.rowcount>1 :
    print("data count: %s" % cursor.rowcount)
    for eachdata in data:
        print ("name : %s " % eachdata['name'], "age : %s " % eachdata['age'])
else:
    print ("name : %s " % data['name'], "age : %s " % data['age'])
 
# 关闭数据库连接
db.close()

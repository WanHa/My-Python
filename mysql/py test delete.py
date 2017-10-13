import pymysql

db=pymysql.connect(host='127.0.0.1',port=3306,user='wh',password='123456',db='test', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
sql="delete from test.node_user where name='Wilson'"
cursor.execute(sql)
db.commit()
db.close()
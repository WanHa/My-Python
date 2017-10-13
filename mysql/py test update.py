import pymysql

db=pymysql.Connection(host='localhost',port=3306,user='wh',password='123456',db='test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

cursor=db.cursor()
sql="update test.node_user set name='wh' where name='Mohan'"
cursor.execute(sql)
db.commit()
db.close()
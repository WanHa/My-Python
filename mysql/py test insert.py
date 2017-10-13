import pymysql
import uuid

db=pymysql.connect(host='127.0.0.1',port=3306,user='wh',password='123456',db='test', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
newid=uuid.uuid4().urn.replace('urn:uuid:','')
cursor=db.cursor()
sql = """INSERT INTO test.node_user(id,name, age) VALUES ('""" + newid + """', 'Mohan', 20)"""

cursor.execute(sql)
db.commit()
db.close()
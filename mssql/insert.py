import pymssql

conn = pymssql.connect("localhost", "wh", "123456", "test")
cursor = conn.cursor()


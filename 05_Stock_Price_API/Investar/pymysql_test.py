import pymysql


class db_con:
    host = 'localhost',
    user = 'root',
    password = 'password',
    charset = 'utf8',
    db = 'myDB'


conn = pymysql.connect(host='localhost', user='root', password='kist', charset='utf8', port=3306)
cursor = conn.cursor()

sql = "CREATE DATABASE developer"

cursor.execute(sql)

conn.commit()
conn.close()

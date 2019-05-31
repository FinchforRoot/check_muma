import MySQLdb
db = MySQLdb.connect(host='localhost', user='root', password='123', database='python', port=3306)
cursor = db.cursor()
sql = """
insert into web (id,url,is_safe) values (1,'https://www.sencx.com',1)
"""
cursor.execute(sql)
db.commit()
db.close()
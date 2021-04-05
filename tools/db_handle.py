import sqlite3

con = sqlite3.connect('E:\WeGame\ocr-service\db.sqlite3')
cursor = con.cursor()


cursor.execute('DELETE FROM website_task')
con.commit()
# 改数据
# cursor.execute('UPDATE my_info set name="李黄绿",age=200 WHERE name="李白"')
# con.commit()
#
# #查数据
# cursor.execute('SELECT * FROM website_task')
# result = cursor.fetchone()
# print(result)

# cursor.execute('SELECT * FROM my_info')
# result = cursor.fetchmany(2)
# print(result)

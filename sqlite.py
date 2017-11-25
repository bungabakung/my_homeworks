import sqlite3

conn = sqlite3.connect('articles.sqlite') #это название базы данных
cur = conn.cursor()

cur.execute('SELECT * FROM articles') #это одна из табличек базы данных
rows = cur.fetchall()

for row in rows:
    print(row)

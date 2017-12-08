import sqlite3

conn = sqlite3.connect('articles.sqlite')
cur = conn.cursor()

title = input("title: ")
url = input("url: ")

cur.execute('INSERT INTO articles (title, url) VALUES (?, ?)', [title, url])
conn.commit()

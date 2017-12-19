#эта программа заполняет в нашей базе данных таблицу
#слова (id, Lemma, Wordform, Glosses)

import sqlite3

conn = sqlite3.connect('hittite.db')
cur = conn.cursor()

conn_2 = sqlite3.connect('gloss_decode.db')
cur_2 = conn_2.cursor()

for i, j, k in cur.execute('SELECT Lemma, Wordform, Glosses FROM wordforms'):
    cur_2.execute('INSERT INTO words (Lemma, Wordform, Glosses)\
VALUES (?, ?, ?)', [i, j, k])
conn_2.commit()

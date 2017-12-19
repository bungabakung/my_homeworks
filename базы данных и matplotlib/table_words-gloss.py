import sqlite3

conn = sqlite3.connect('gloss_decode.db')
cur = conn.cursor()

conn_2 = sqlite3.connect('gloss_decode.db')
cur_2 = conn_2.cursor()

conn_3 = sqlite3.connect('gloss_decode.db')
cur_3 = conn_3.cursor()
di = {}
for i, k in cur.execute('SELECT id, gloss FROM gloss_decode_table'):
    di[k] = i
print(di)

for row in cur.execute('SELECT * FROM words'):
    for j in row[3].split('.'):
        if j.isupper():
            print(str(row[0]))
            print(j)
            cur_2.execute('INSERT INTO wordsgloss (wordid, glossid) VALUES (?, ?)', [row[0], di[j]])

conn_2.commit()


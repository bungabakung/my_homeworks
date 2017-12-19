#эта программа добавляет в табличку базы данных с глоссами и расшифровками,
#которых нет в txt, но которые встретились в данной нам базе данных

import sqlite3

conn = sqlite3.connect('hittite.db')
cur = conn.cursor()
gloss_arr = []

for row in cur.execute('SELECT Glosses FROM wordforms'):
    row_2 = str(row)[2:-3]
    row_arr = row_2.split('.')
    for i in row_arr:
        if i.isupper() and i not in gloss_arr:
            gloss_arr.append(i)

        
conn_2 = sqlite3.connect('gloss_decode.db')
cur_2 = conn_2.cursor()

arr_help = []
for j in cur_2.execute('SELECT gloss FROM gloss_decode_table'):
    arr_help.append((str(j)[2:-3]))


for x in gloss_arr:
    if x not in arr_help:
        cur_2.execute('INSERT INTO gloss_decode_table (gloss, gl_dec)\
VALUES (?, ?)', [x, '?'])
conn_2.commit()        
    

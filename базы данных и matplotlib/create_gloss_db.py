#эта программа записывает в табличку базы данных те глоссы, которые нам даны в txt, и их расшифровки

import sqlite3

conn = sqlite3.connect('gloss_decode.db')
cur = conn.cursor()

with open('Glossing_rules.txt', 'r', encoding = 'utf-8') as text:
    a = text.readlines()
    for line in a:
        gloss = ''
        gl_dec = ''
        for i in range(len(line)):
            if line[i] == '—':
                break
        gloss = line[:i-1]
        print(gloss)
        gl_dec = line[i+2:]
        print(gl_dec)
        cur.execute('INSERT INTO gloss_decode_table (gloss, gl_dec) VALUES (?, ?)', [gloss, gl_dec])
        conn.commit()
        
        

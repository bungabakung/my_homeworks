#эта программа выводит только 1 график сразу
#но с названием и подписями к осям

import sqlite3
import matplotlib
import matplotlib.pyplot as plt


Cases = ["LOC", "NOM", "GEN", "DAT", "ACC", "DAT-LOC",\
         "INSTR", "ABL", "VOC"]

conn = sqlite3.connect('gloss_decode.db')
cur = conn.cursor()

di = {} #это типа частотный словарь
#но не у всех частей речи есть эксплицитная глосса, говорящая,
#какой части речи это слово, поэтому, напр., сущ. и гл. сюда не вошли
for i in cur.execute('SELECT glossid FROM wordsgloss'):
    if str(i)[1:-2] not in di:
        di[str(i)[1:-2]] = 1
    else:
        di[str(i)[1:-2]] += 1

di_2 = {} #сейчас ещё создадим словарь id глоссы -- сама глосса
for i, j in cur.execute('SELECT id, gloss FROM gloss_decode_table'):
    di_2[str(i)] = j



A = []
B = []
for j in di:
    if di_2[j] in Cases:
        A.append(di_2[j])
        B.append(di[j])



plt.bar(A, B)
plt.title('Частотность по падежам')
plt.ylabel('падежи')
plt.xlabel('части речи')

plt.show()

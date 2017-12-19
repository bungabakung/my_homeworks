import sqlite3
import matplotlib
import matplotlib.pyplot as plt

POS = ["ADJ", "ADV", "AUX", "COMP", "CONJ", "CONN", "DEM",\
       "INDEF", "N", "NEG", "NUM", "P", "PART", "POSS",\
       "PRON", "PRV", "PTCP", "REL", "Q", "V"]
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



X = []
Y = []
for j in di:
    if di_2[j] in POS:
        X.append(di_2[j])
        Y.append(di[j])



A = []
B = []
for j in di:
    if di_2[j] in Cases:
        A.append(di_2[j])
        B.append(di[j])


flg, ax = plt.subplots(nrows = 2, ncols = 1)

ax[0].bar(X, Y)
#ax[0].title('Частотность по частям речи')
#ax[0].ylabel('частотность')
#ax[0].xlabel('части речи')

ax[1].bar(A, B)
#ax[1].title('Частотность по падежам')
#ax[1].ylabel('падежи')
#ax[1].xlabel('части речи')

plt.show()

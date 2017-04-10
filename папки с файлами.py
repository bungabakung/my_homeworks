import os
import shutil
number = int(input('Введите число '))
a = 0
for i in range(1, number+1):
    if os.path.exists(str(i)):
        shutil.rmtree(str(i))
    os.mkdir(str(i))
    for c in range(i):
        f = open(str(i) + '\\' + str(a) + '.txt', 'w', encoding = 'utf-8')
        a += 1

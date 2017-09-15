## программа лежит в той же папке, где файлы со статьями
import os
import re
import codecs
f1 = open('file_words.txt', 'w', encoding = 'utf-8')
for file in os.listdir('.'):
    if file.endswith('xhtml'):
        f = codecs.open(file, 'r', 'Windows-1251')
        a = f.read()
        f.close()
        r = re.search('<title>(.*)</title>', a)
        if r:
            f1.write(r.group(1) + '\t' + str(len(re.findall('<w>', a))) + '\n')
        print('1')
f1.close()

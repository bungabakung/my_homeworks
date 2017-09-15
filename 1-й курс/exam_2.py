import os
import re
import codecs
f2 = open('table.csv', 'w', encoding = 'utf-8')
f2.write('Название текста' + ',' + 'Автор' + ',' 'Дата создания текста')
for file in os.listdir('.'):
    if file.endswith('xhtml'):
        with codecs.open(file, 'r', 'Windows-1251') as f:
            a = f.read()
            f.close()
            r1 = re.search('<title>(.*)</title>', a)
            r2 = re.search('<meta content=\"(.*)\" name=\"author\"/>', a)
            r3 = re.search('<meta content=\".*\" name=\"created\"></meta>', a)
            if r1 and r2 and r3:
                f2.write(r1.group(1) + ',' + r2.group(1) + ',' + r3.group(1))
f2.close()

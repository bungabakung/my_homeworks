import re

def func1():
    d = {}
    f = open('тестовый файл.txt', 'r', encoding = 'utf-8')
    a = f.readlines()
    for line in a:
        line = re.sub('(\.\.?\.?|\?|!)(\n)? ?', '.', line)
        sentences = line.split('.')
        for sentence in sentences:
            if len(sentence) >= 1:
                d[sentence] = {word.strip(): len(word.strip())\
                               for word in sentence.split(' ')}
    return d

print(func1())
        

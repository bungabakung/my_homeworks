import pymorphy2
from pymorphy2 import MorphAnalyzer
import json
import re

morph = MorphAnalyzer()

array = []


with open ('1grams-3.txt', 'r', encoding = 'utf-8') as f:
    a = f.readlines()
    for line in a:
        arr = line.split('\t')
        form = arr[1].replace('\n', '')
        array.append(form)

lemmas = [] #леммы (для контроля, \
#что одна лемма не попадёт 2 раза)
n_lemmas = [] #леммы с разборами


y = 0
i = 0

while y <= 1000:
    
    ana = morph.parse(array[i])
    first = ana[0]
    if first.normal_form not in lemmas:
        lemmas.append(first.normal_form)
        n_lemmas.append(first.normalized)
        y += 1

    i += 1



n_dict = {}

for n in n_lemmas:
    n_dict[str(n.tag)] = []

for n in n_lemmas:
    n_dict[str(n.tag)].append(n.word)



with open('file.json', 'w', encoding = 'utf-8') as f:
    json.dump(n_dict, f, ensure_ascii = False)


        
    

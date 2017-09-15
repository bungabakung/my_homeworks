import re

def func2():
    arr = [] 
    f = open('text.xml', 'r', encoding = 'utf-8') 
    a = f.read()
    f.close() 
    arr = [i.group(1) for i in re.finditer('gr=\"([A-Z]*)(,|=)', a)]
    return arr

def freq_dict(arr):
    word_count = {} 
    for word in arr: 
         if word not in word_count: 
             word_count[word] = 1 
         else: 
             word_count[word] += 1 
    return word_count

def func3(freq_dict):
    f = open('freq_dict.txt', 'w', encoding = 'utf-8')
    for x in freq_dict:
        f.write(x + '\t' + str(freq_dict[x]) + '\n')
    f.close()
    return

func3(freq_dict(func2()))

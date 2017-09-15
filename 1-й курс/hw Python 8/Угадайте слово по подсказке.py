import random

def length(string):
    s1 = ''
    i = 0
    for i in range(len(string)):
        s1 += '.'
    return s1

def create_arr_and_dic():
    f = open("Слова и подсказки.csv", encoding = "utf-8")
    a = f.readlines()
    arr = []
    dic = {}
    for line in a:
        words = line.split(';')
        x = words[0].strip('\ufeff')
        arr.append(x)
        dic[x] = words[1].strip('\n')
    return arr, dic

array, dictionary = create_arr_and_dic()  
y = random.choice(array)
print('Вот ваша подсказка:', y, length(y))
z = input('Загаданное слово: ')
if z == dictionary[y]:
    print('Правильно.')
else:
    print('Увы, нет:(')


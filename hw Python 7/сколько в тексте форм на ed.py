def func1(text_file):
    ed = 0
    y = 0
    i = 0
    f = open(text_file, encoding = "utf-8")
    a = f.readlines()
    for line in a:
        words = line.split()
        for i in range(len(words)):
            if words[i].endswith('ed'):
                ed += 1
            if words[i].endswith('ied'):
                y += 1
    arr = []
    arr.append(ed)
    arr.append(y)
    return arr

a = input('Введите название файла, который хотите открыть: ')
print('Количество форм на -ed в тексте: ', func1(a)[0], \
'\nИз них образованы от глаголов на -y: ', func1(a)[1])

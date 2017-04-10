def func1():
    arr = []
    i = 0
    f = open("1.txt", 'r', encoding = "utf-8")
    a = f.readlines()
    for line in a:
        words = line.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
            arr.append(words[i].strip(',.()«»!'))
    f.close()
    arr.sort()
    return arr

def freqdict(arr):
    word_count = {}
    for word in arr:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

f1 = open("2.tsv", 'w', encoding = "utf-8")
for j in sorted(freqdict((func1()))):
    f1.write(j)
    f1.write('\t')
    f1.write(str(freqdict(func1())[j]))
    f1.write('\n')
f1.close()

alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = list(alphabet)

def freqdict1(arr):
    letter_count = {}
    for letter in alphabet:
        letter_count[letter] = 0
        for word in arr:
            if word.startswith(letter):
                letter_count[letter] += 1
    return letter_count

f2 = open("3.tsv", 'w', encoding = "utf-8")
for k in sorted(freqdict1(func1())):
    f2.write(k)
    f2.write('\t')
    f2.write(str(freqdict1(func1())[k]))
    f2.write('\n')
f2.close()
    

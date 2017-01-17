def func1():
    arr=[]
    i=0
    f=open("1.txt", encoding="utf-8")
    a=f.readlines()
    for line in a:
        words=line.split()
        for i in range(len(words)):
            words[i]=words[i].lower()
            arr.append(words[i].strip('.,!?/\|()";:'))
    f.close()
    return arr

def freqdict(arr):
    word_count = {}
    for word in arr:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

for word in freqdict(func1()):
    if freqdict(func1())[word] >= 10:
        print (word, freqdict(func1())[word])


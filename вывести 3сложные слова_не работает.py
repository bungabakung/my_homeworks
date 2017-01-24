import re

def func1():
    arr = []
    i = 0
    f = open("1.txt", encoding = "utf-8")
    a = f.readlines()
    for line in a:
        words = line.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
            arr.append(words[i].strip('.,!?/\|()";:'))
    f.close()
    return arr

i = 0
for i in range(len(func1())):
    if '.*[аяоёуюэеыиАЯОЁУЮЭЕЫИ].*[аяоёуюэеыи]\.*[аяоёуюэеыи].*' \
       == func1()[i]:
        print(func1()[i])
print (x)

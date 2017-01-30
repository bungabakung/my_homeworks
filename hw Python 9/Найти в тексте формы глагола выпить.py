import re

def func1():
    arr = []
    i = 0
    f = open("Текст с глаголом выпить.txt", encoding = "utf-8")
    a = f.readlines()
    for line in a:
        words = line.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
            arr.append(words[i].strip('.,!?/\|()";:'))
    f.close()
    return arr

arr1 = []
i = 0
for i in range(len(func1())):
    if re.search('вып((ей(те)?)|(ь(е((шь)|м|те?)|ют?))|(и((л(а|о|и)?)|(т(ь?|(ы(й|ми?|х|е))\
|(ая?)|(о(е|(го)|й|му?)?)|(ую))))|в(ш((ая)|(ую)|и(й|ми?|х)|е(е|ю|му?)))?))', func1()[i]):
        if func1()[i] not in arr1:
            arr1.append(func1()[i])
            print(func1()[i])


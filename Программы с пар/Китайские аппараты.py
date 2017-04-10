import re

def func1():
    arr = []
    i = 0
    f = open("Космическая программа Китая.txt", encoding = "utf-8")
    a = f.readlines()
    for line in a:
         arr.append(line)
    f.close()
    return arr

i = 0
arr1 = []
for i in range(len(func1())):
    res = re.findall('«[А-Яа-я ]*-[1-9]»', func1()[i])
    j = 0
    for j in range(len(res)):
        if res[j] not in arr1:
            arr1.append(res[j])
            print (res[j])

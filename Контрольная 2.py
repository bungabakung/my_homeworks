import re

def func0():
    f1 = open("Из исландского корпуса.xml", 'r', encoding = "utf-8")
    a = f1.readlines()
    f1.close()
    f2 = open("Количество строк.txt", 'w', encoding = "utf-8")
    f2.write(str(len(a)))
    f2.close()
    return a

func0()

def func1():
    freqdict = {}
    for line in func0():
        s1 = re.search("<w lemma=\".+\" type=\"(.+)\">.+</w>", line)
        if s1:
            if s1.group(1) not in freqdict:
                freqdict[s1.group(1)] = 1
            else:
                freqdict[s1.group(1)] += 1
    return freqdict

def func2():
    f3 = open("Ключи.txt", 'w', encoding = "utf-8")
    for i in func1():
        f3.write(i)
        f3.write('\n')
    f3.close()
    return True

func2()

def func3():
    f4 = open("Прилагательные.txt", 'w', encoding = "utf-8")
    for i in func1():
        s2 = re.search("l.f...", i)
        if s2:
            f4.write(i)
            f4.write(' ')
            f4.write(str(func1()[i]))
            f4.write('\n')
    f4.close()
    return True

func3()

def func4():
    f5 = open("Внутри тега body.txt", 'r', encoding = "utf-8")
    change1 = re.sub("<w lemma=\"(.+)\" type=\"(.+)\">(.+)</w>", "\\1 \\2 \\3", f5.read())
    change2 = re.sub("<.*>", ' ', change1)
    f5.close()
    return change2



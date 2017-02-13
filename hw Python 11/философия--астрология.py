import re

def func1():
    f1 = open("Философия -- Википедия.txt", 'r', encoding = "utf-8")
    change1 = re.sub('Филос(о́|о)фи(я(х|ми?)?|и|е?й|ю)', 'Астрол\\1ги\\2', f1.read())
    change2 = re.sub('философи(я(х|ми?)?|и|е?й|ю)', 'астрологи\\1', change1)
    f1.close()
    return change2

def func2():
    f2 = open("Астрология.txt", 'w', encoding = "utf-8")
    f2.write(func1())
    f2.close()
    return True

func2()

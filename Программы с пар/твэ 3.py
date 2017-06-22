import re

def func3b(string):
    r = re.match('<w>([А-Яа-я][a-я]*)<ana', string)
    if r:
        x = r.group(1)
    else:
        x = ''
    return x



def func4():
    f1 = open('text.xml', 'r', encoding = 'utf-8')
    f2 = open('S_ins.txt', 'w', encoding = 'utf-8')
    a = f1.readlines()
    j = 0
    for line in a:
        if not '<w' in line:
            a.pop(j)
        j += 1
    f1.close()            
    i = 0
    for i in range(len(a)):
        if '<w' and 'S' and 'ins' in a[i]:
            f2.write (func3b(a[i-3]) + ' '\
                      + func3b(a[i-2]) + ' '\
                      + func3b(a[i-1]) + '\t'\
                      + func3b(a[i]) + '\t'\
                      + func3b(a[i+1]) + ' '\
                      + func3b(a[i+2]) + ' '\
                      + func3b(a[i+3]) + '\n')
    f2.close()

func4()

import re

def func1():
    f = open('text.xml', 'r', encoding = 'utf-8')
    a = f.readlines()
    f.close()
    w_sum = 0
    arr1 = []
    ana_sum = 0
    arr2 = []
    for line in a:
        arr1 = re.findall('<w>.+</w>', line)
        w_sum += len(arr1)
        arr2 = re.findall('ana', line)
        ana_sum += len(arr2)
    print (str(ana_sum/w_sum))
    return

func1()

import os

def func1():
    freqdict = {}
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            if d[0] in freqdict:
                freqdict[d[0]] += 1
            else:
                freqdict[d[0]] = 1
    return freqdict

def func2(freqdict):
    x = 0
    for i in freqdict:
        if freqdict[i] > x:
            x = freqdict[i]
            a = i
    print ('название большинства папок начинается на ' + a)
    return

func2(func1())
    

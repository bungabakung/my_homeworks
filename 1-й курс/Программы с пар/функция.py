def func1():
    arr=[]
    num=0
    i=0
    f=open("1.txt", encoding="utf-8")
    a=f.readlines()
    for line in a:
        words=line.split()
        for i in len(words):
            words[i]=words[i].lower()
            arr[i]=words[i].strip('.,!?/\|()";:')
        num+=len(words)
    f.close()
    return num    
b=func1()
print(b)

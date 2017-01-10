def func1():
    arr=[]
    i=0
    f=open("1.txt", encoding="utf-8")
    a=f.readlines()
    for line in a:
        words=line.split()
        for i in range(len(words)):
            words[i]=words[i].lower()
            words[i]=words[i].strip('.,!?/\|()";:')
            arr.append(words[i])
    f.close()
    return arr

def func2(x,arr):
    glasnye='аяоёуюэеыи'
    slova=[]
    i=0
    for i in range(len(arr)):
        j=0
        slogi=0
        for j in range(len(arr[i])):
            if arr[i][j] in glasnye:
                slogi+=1
        if slogi==x:
            slova.append(arr[i])
    return slova

y=int(input('Введите натуральное число '))
print(func2(y,func1()))


    




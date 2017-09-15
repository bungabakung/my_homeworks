import os

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. '

def func1():
    
    number = 0
    arr1 = []

    for i in os.listdir('.'):
        if os.path.isfile(i):
            j = 0
            check1 = True
            check2 = 0
            for j in range(len(i)):
                if i[j] not in alphabet:
                    check1 = False
                if i[j] == '.':
                    check2 += 1
            if check1 == True and check2 <= 1:
                number += 1
                arr1.append(i)

    print('Найдено файлов, название которых состоит \
только из латинских символов: ' + str(number))
    
    return arr1

def func2(arr):

    arr2 = []

    for i in arr:
        if i[0:i.find('.')] not in arr2:
            arr2.append(i[0:i.find('.')])
            
    for k in arr2:
        print (k)

    return

func2(func1())

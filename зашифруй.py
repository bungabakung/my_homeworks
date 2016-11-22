ss=[]
string=''
latinica='abcdefghijklmnopqrstuvwxyz'
LATINICA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
kirillica='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
KIRILLICA='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s=input('Введите что-нибудь ')
while len(s)!=0:
    for i in range(len(s)):
        if s[i] in latinica:
            for j in range(len(latinica)):
                if s[i]==latinica[j]:
                    if j==len(latinica)-1:
                        string+=latinica[1]
                    else:
                        string+=latinica[j+1]
        elif s[i] in LATINICA:
            for j in range(len(LATINICA)):
                if s[i]==LATINICA[j]:
                    if j==len(LATINICA)-1:
                        string+=LATINICA[1]
                    else:
                        string+=LATINICA[j+1]
        elif s[i] in kirillica:
            for j in range(len(kirillica)):
                if s[i]==kirillica[j]:
                    if j==len(kirillica)-1:
                        string+=kirillica[1]
                    else:
                        string+=kirillica[j+1]
        elif s[i] in KIRILLICA:
            for j in range(len(KIRILLICA)):
                if s[i]==KIRILLICA[j]:
                    if j==len(KIRILLICA)-1:
                        string+=KIRILLICA[1]
                    else:
                        string+=KIRILLICA[j+1]
        else:
            string+=(s[i])
    print(string,' ')
    string=''
    s=input('Введите что-нибудь ')
print('Вы ничего не ввели, программа идет спать')

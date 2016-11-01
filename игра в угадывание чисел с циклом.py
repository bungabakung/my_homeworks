a=9
a=int(a)
s=input('Введите число ')
if len(s)==0:
    print ('Game over')
s=int(s)
while a!=s:
    if a>s:
        print('Загаданное число больше')
    if a<s:
        print ('Загаданное число меньше')
    s=input('Попробуйте еще раз ')
    s=int(s)
print('Позравляю, вы угадали')



    

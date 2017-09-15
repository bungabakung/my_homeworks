word=input('Введите слово ')
anotherword=''
sameword=word
print(word)
for i in range(len(word)-1):
    anotherword=word[len(word)-i-1]
    for k in range(len(sameword)-1):
        anotherword+=sameword[k]
    print(anotherword)
    sameword=anotherword

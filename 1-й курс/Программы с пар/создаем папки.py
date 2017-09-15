import os
s = input('Введите предложение на английском ')
words = s.split(' ')
path = ''
for word in range(len(words)-1):
    path += words[word]
    path += '\\'
path += words[len(words)-1]
os.makedirs(path)

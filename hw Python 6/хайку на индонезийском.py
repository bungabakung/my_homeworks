import random

def actor3():
    slova=[]
    f=open('actor3.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    slovo=random.choice(slova)
    slovo=slovo.capitalize()
    return slovo

def adj2():
    slova=[]
    f=open('adj2.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    return random.choice(slova)

def line1(noun, adjective):
    return noun + ' ' + adjective

def adverb2():
    slova=[]
    f=open('adverb2.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    slovo=random.choice(slova)
    slovo=slovo.capitalize()
    return slovo

def verb2():
    slova=[]
    f=open('verb2.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    return random.choice(slova)

def place2():
    slova=[]
    f=open('place2.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    return random.choice(slova)

def line2(adverb, verb, place):
    return adverb + ' ' + verb + ' di ' + place + '.'

def actor2():
    slova=[]
    f=open('actor2.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    slovo=random.choice(slova)
    slovo=slovo.capitalize()
    return slovo

def verb3():
    slova=[]
    f=open('verb3.txt', encoding="utf-8")
    a=f.readlines()
    z=0
    for line in a:
        words=line.split()
        for z in range(len(words)):
            slova.append(words[z])
        z=0
    return random.choice(slova)

def line3(noun, verb):
    return noun + ' ' + verb + '.'

def randomhaiku():
    haiku = line1(actor3(), adj2()) +\
            '\n' + line2(adverb2(), verb2(), place2()) +\
            '\n' + line3(actor2(), verb3())
    return haiku

print (randomhaiku())






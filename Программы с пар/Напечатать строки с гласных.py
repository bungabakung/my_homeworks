f=open("Vojna i mir. Tom 1.txt",'r',encoding="utf-8")
glasnye='АаЕеЁёИиОоУуЫыЭэЮюЯя'
a=f.readlines()
for i in a:
    if i[0] in glasnye:
        print(i)
f.close()

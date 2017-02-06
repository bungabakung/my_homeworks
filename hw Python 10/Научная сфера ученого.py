import re

def func1():
    f = open("Ферма, Пьер — Википедия.html", encoding = "utf-8")
    arr = []
    i = 0
    a = f.readlines()
    for line in a:
         arr.append(line)
    f.close()
    return arr

def func2():
    i = 0
    for i in range(len(func1())):
        r1 = re.search("<th style=\"min-width:9em;\">Научная сфера:</th>", func1()[i])
        r2 = re.search("<td class=\"\" style=\"\">", func1()[i+1])
        if r1 and r2:
            r = re.search("(<p><span class=\"no-wikidata\" data-wikidata-property-id=\"P101\">\
<a href=\"https://ru.wikipedia.org/.*\" title=\")(.*)(\">.*</a></span></p>)", \
                      func1()[i+2])
            break
    return r

def func3():
    if func2():
        title = func2().group(2)
    else:
        print ('что-то пошло не так')
    return title

f = open("text_wiki.txt", 'w', encoding = "utf-8")
f.write(func3())
f.close()

f = open("text_wiki.txt", encoding = "utf-8")
a = f.readlines()
for line in a:
    print(line)

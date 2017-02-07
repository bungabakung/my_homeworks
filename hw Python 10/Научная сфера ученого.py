import re

def func1():
    f = open("Ферма, Пьер — Википедия.html", encoding = "utf-8")
    a = f.readlines()
    i = 0
    for i in range(len(a)):
        r1 = re.search("<th style=\"min-width:9em;\">Научная сфера:</th>", a[i])
        r2 = re.search("<td class=\"\" style=\"\">", a[i+1])
        if r1 and r2:
            r = re.search("(<p><span class=\"no-wikidata\" data-wikidata-property-id=\"P101\">\
<a href=\"https://ru.wikipedia.org/.*\" title=\")(.*)(\">.*</a></span></p>)", \
                      a[i+2])
            break
    f.close()
    return r

def func2():
    if func1():
        title = func1().group(2)
    else:
        print ('что-то пошло не так')
    return title

f = open("text_wiki.txt", 'w', encoding = "utf-8")
f.write(func2())
f.close()

f = open("text_wiki.txt", encoding = "utf-8")
a = f.readlines()
for line in a:
    print(line)

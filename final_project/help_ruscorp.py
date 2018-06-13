import urllib.request
import re
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import render_template



decode = {'а': '%E0', 'б': '%E1', 'в': '%E2', 'г': '%E3', 'д': '%E4', 'е': '%E5',\
          'ё': '%B8', 'ж': '%E6', 'з': '%E7', 'и': '%E8', 'й': '%E9',\
          'к': '%EA', 'л': '%EB', 'м': '%EC', 'н': '%ED', 'о': '%EE',\
          'п': '%EF', 'р': '%F0', 'с': '%F1', 'т': '%F2', 'у': '%F3',\
          'ф': '%F4', 'х': '%F5', 'ц': '%F6', 'ч': '%F7', 'ш': '%F8',\
          'щ': '%F9', 'ъ': '%FA', 'ы': '%FB', 'ь': '%FC', 'э': '%FD', 'ю': '%FE', 'я': '%FF'}

def old_poem(some_word):
    arr = []
    for i in list(some_word):
        arr += decode[i]
        word = ''.join(arr)

    req = urllib.request.Request('http://search1.ruscorpora.ru/search.xml?sort=\
gr_created&out=normal&dpp=10&spd=10&seed=\
14286&env=alpha&mycorp=&mysent=&mysize=\
&mysentsize=&mydocsize=&text=lexgramm&mode=\
poetic&ext=10&nodia=1&parent1=0&level1=\
0&lex1=' + word + '&gramm1=&flags1=\
&sem1=&parent2=0&level2=\
0&min2=1&max2=1&lex2=&gramm2=&flags2=&sem2=')

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')

    
    r = re.search('<span class="b-doc-expl" explain="([0-9]+)">', html)
    if r:
        number = r.group(1)

    req_1 = urllib.request.Request('http://search1.ruscorpora.ru/search.xml?sort=\
gr_created&out=normal&dpp=10&spd=10&seed=10216\
&env=alpha&mycorp=&mysent=&mysize=&mysentsize=\
&mydocsize=&text=lexgramm&mode=\
poetic&ext=10&nodia=1&parent1=0&level1=\
0&lex1=' + word + '&gramm1=&flags1=\
&sem1=&parent2=0&level2=\
0&min2=1&max2=1&lex2=&gramm2=&flags2=&sem2=&docid=' + number + '&sid=9&expand=full')

    with urllib.request.urlopen(req_1) as response_1:
        html_1 = response_1.read().decode('windows-1251')

    soup = BeautifulSoup(html_1, 'html.parser')
    text = soup.get_text()

    arr_1 = text.split('  ')


    for i in range(len(arr_1)):
        if arr_1[i].startswith('Результаты поиска'):
            j = i
            break

    arr_2 = []
    for i in range(j+2, len(arr_1)-2):
        arr_2.append(arr_1[i])

    #final = ''
    #for i in arr_2:
        #final += i
        #final += '\n'

    return arr_2


app = Flask(__name__)

@app.route('/')
def find():
    if request.args.get('word'):
        poem = old_poem(request.args.get('word'))
        len_a = len(poem)
        return render_template('result_page.html', len_a = len_a, poem = poem)
    return render_template('final_project.html')

if __name__ == '__main__':
    import os
    app.run(debug = True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

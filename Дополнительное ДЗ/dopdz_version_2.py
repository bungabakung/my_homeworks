import urllib.request
import re
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os
import html
import bs4
from bs4 import BeautifulSoup


#на будущее -- сделаем словарь, чтобы было удобно ходить по сайту со словарём
#дореволюционной орфографии (я просто посмотрела, как там устроены адреса
#страниц со словами на определённую букву)
di = {}
alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
code_16 = list('0123456789abcdef')
for i in range(len(alphabet)):
    if i <= 15:
        di[alphabet[i]] = r'http://www.dorev.ru/ru-index.html?l=' + 'c' + code_16[i]
    else:
        di[alphabet[i]] = r'http://www.dorev.ru/ru-index.html?l=' + 'd' + code_16[i-16]


req = urllib.request.Request('https://www.gismeteo.ru/weather-skopje-3253/now/')
with urllib.request.urlopen(req) as response:
   my_html = response.read().decode('utf-8')
#скачиваем страницу Gismeteo с погодой в Скопье

weather_search = re.search('((\+|-)[0-9])<span class="tab-weather__value_m">(,[0-9])</span>', my_html)
if weather_search:
    true_weather = weather_search.group(1) + weather_search.group(3)
else:
    true_weather = 'Сейчас не удаётся определить погоду'
#достаём из этой страницы погоду в Скопье сейчас
print(true_weather)


app = Flask(__name__)


def adj(word_1, word_2):
    if word_1.endswith('ые') or word_1.endswith('ие') \
               or word_1.endswith('ыеся') or word_1.endswith('иеся'):
        with open('next_word.txt', 'w', encoding = 'utf-8') as f4:
            f4.write(word_2)
        os.system(r'C:\Users\lilia\Downloads\mystem.exe -cid next_word.txt nw_output.txt')
        with open('nw_output.txt', 'r', encoding = 'utf-8') as f5:
            a5 = f5.read()
        if 'жен' in a5 or 'сред' in a5:
            return True
        else:
            return False
    else:
        return False


def adj2(word):
    corr_word = re.sub('(ы|i)е(ся|)', '\\1я\\2', word)
    return corr_word


def old_orth(word):
    with open(r'C:\Users\lilia\Downloads\got_word.txt', 'w', encoding = 'utf-8') as f1:
        f1.write(word)
    result_word = ''
    glasnye = 'ыиэеаяоёуюй'
    soglasnye = 'бвгджзклмнпрстфхцчшщ'
    for i in range(len(word)): #меняем и на i
        if word[i] == 'и' and i != len(word)-1:
            if word[i+1] in glasnye:
                result_word += 'i'
            else:
                result_word += word[i]
        else:
            result_word += word[i]
    if word[len(word)-1] in soglasnye: #добавляем ъ в конце
        result_word += 'ъ'
    #исправляем написание приставок
    if word.startswith('бес') or word.startswith('чрес') or word.startswith('черес'):
        result_word = re.sub('(бе|чре|чере)с', '\\1з', result_word)

        
    #ох щас ещё Mystem прикрутим
    os.system(r'C:\Users\lilia\Downloads\mystem.exe -cid C:\Users\lilia\Downloads\got_word.txt C:\Users\lilia\Downloads\output.txt')
    with open(r'C:\Users\lilia\Downloads\output.txt', 'r', encoding = 'utf-8') as f2:
        read_output = f2.read()
        if word.endswith('е') and ('дат' in read_output or 'пр' in read_output): #исправляем окончание дат и пр
            result_word = result_word[:-1] + 'ѣ'
        #определяем словарную форму слова
        r = re.search('{(.+?)=', read_output)
        if r:
            lemma = r.group(1)
        else:
            lemma = result_word
        #lemma_cp1251 = str(lemma.encode('cp1251')) -- это оказалось лишним
        #lemma_cp1251 = lemma_cp1251.strip("b'").replace(r'\x','%')
        #открываем нужную страницу в словаре
        req_1 = urllib.request.Request(di[lemma.lower()[0]])
        

        if 'е' in word or 'ф' in word or 'и' in word:
           with urllib.request.urlopen(req_1) as response_1:
                my_html_1 = response_1.read().decode('cp1251')
                html_string = re.search('<td class="uu">' + lemma + \
                            '</td><td></td><td class="uu">(.*?)</td>', my_html_1)
                if html_string:
                     nechto = html_string.group(1)
                     nechto = re.sub('<.*?>', '', nechto)
                     nechto = re.sub('\(.*?\)', '', nechto)
                     nechto = re.sub('\'', '', nechto)
                     nechto = re.sub('&#1123;', 'ѣ', nechto)
                     nechto = re.sub('&#1139;', 'ѳ', nechto)
                     nechto = re.sub('&#1110;', 'i', nechto)
                     nechto = re.sub('&#1141;', 'ѵ', nechto)
                     for d in range(len(nechto)):
                         if nechto[d] == ',':
                             nechto = nechto[:d]
                             break
                     print(nechto)

                     try:
                         res_word = list(result_word)
                         for z in range(len(nechto)):
                         
                                 if nechto[z] == 'ѣ' or nechto[z] == 'ѳ' or nechto[z] == 'i'\
                                or  nechto[z] == 'ѵ':
                                     res_word[z] = nechto[z]
                         result_word = ''
                         for v in res_word:
                             result_word += v
                             
                     except IndexError:
                          result_word = result_word
                         
    return result_word


@app.route('/1stpage')
def page_1():
    if request.args:
        the_word = request.args['word']
        return render_template('brackets_template_2', old_word = old_orth(the_word))
    return render_template('brackets_template_1', weather = true_weather)


@app.route('/test')
def test():
    summa = 0
    arr = ['хлебъ', 'апрель', 'гнедой', 'дедъ', 'месяцъ', \
           'левъ', 'ледяной', 'пень', 'запретъ', 'семья']
    arr_2 = []
    for i in arr:
        i_1123 = re.sub('е', 'ѣ', i)
        arr_2.append([i, i_1123])
    l = len(arr_2)
    i = 0
    if request.args:
        for i in range(10):
            if 0 <= i <= 4:
                if request.args.get(str(i)) == '1123':
                    summa += 1
            elif 5 <= i <= 9:
                if request.args.get(str(i)) == 'e':
                    summa += 1
        
        return render_template('test_result.html', summa = summa)

    return render_template('dopdz_test_2.html', l = l, arr_2 = arr_2)

@app.route('/news')
def news():

    
    fr_di = {}
    fr_arr = []
    top = 0
    y = 0
    m = 0

    with open('new_final.txt', 'r', encoding = 'utf-8') as new_f:
        a7 = new_f.readlines()
    
    len_7 = len(a7)
    for line in a7:
        if line not in fr_di:
            fr_di[line] = 1
        else:
            fr_di[line] += 1
    for n in range(10):
        for x in fr_di:
            if fr_di[x]  > top and x not in fr_arr:
                top = fr_di[x]
                top_word = x
        fr_arr.append(top_word)
        top = 0
    len_fr_arr = len(fr_arr)

        
        
    return render_template('dopdz_news.html', m = m, a7 = a7, len_7 = len_7, y = y, \
                           fr_arr = fr_arr, len_fr_arr = len_fr_arr)
            
        
    


if __name__ == '__main__':
    app.run(debug = True)

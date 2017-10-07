#объем меньше 100 тысяч слов, потому что мне не удалось найти старые статьи

import urllib.request 
import re
import html
import os

req = urllib.request.Request('http://unecha-gazeta.ru/')
with urllib.request.urlopen(req) as response:
   my_html = response.read().decode('utf-8') #скачиваем главную страницу газеты

categories = re.findall('class="menuitem" href="http://unecha-gazeta.ru/category/.+?">', my_html)

true_categories = []
for cat in categories:
    true_cat = re.sub('class="menuitem" href="(http://unecha-gazeta.ru/category/.+)">', '\\1', cat)
    true_categories.append(true_cat) #получаем массив со ссылками на категории, к которым могут относиться статьи газеты


all_links = []

for true_cat in true_categories:
    req2 = urllib.request.Request(true_cat)
    with urllib.request.urlopen(req2) as response:
        html2 = response.read().decode('utf-8')
    links = re.findall('<a href="http://unecha-gazeta.ru/(.+)"><h3>.+?</h3></a>', html2)
    for link in links:
        if link not in all_links:
            all_links.append(link) #находим рег. выр. со ссылкамии на статьи
 
true_links = []
for link in all_links:
    true_link = re.sub('<a href="http://unecha-gazeta.ru/(.+)"><h3>.+</h3></a>', 'http://unecha-gazeta.ru/' + '\\1', link)
    true_links.append(true_link) #получаем массив с различающимися кусками ссылок

f1 = open('C:\\Users\\lilia\\Documents\\Unechskaya_gazeta\\metadata.csv', 'w', encoding = 'utf-8')
f1.write('path\tauthor\tsex\tbirthday\theader\tcreated\tsphere\tgenre_fi\ttype\ttopic\tchronotop\
         \tstyle\taudience_age\taudience_level\taudience_size\tsource\tpublication\tpublisher\
         \tpubl_year\tmedium\tcountry\tregion\tlanguage\n') #создаем таблицу для метаданных



mega_arr = []


for link in true_links: #проходимся циклом по всем ссылкам из нашего массива
    
    find_date = re.search('(.+)/(....)/(..)/(..).+', link) #дата есть в самой ссылке, находим её 
    if find_date:

        smaller_arr = []
        
        year = find_date.group(2)
        month = find_date.group(3)
        day = find_date.group(4) #узнаём дату, когда была создана статья
         
        dir_name = 'C:\\Users\\lilia\\Documents\\Unechskaya_gazeta\\plain\\' + year + '\\' + month
        if not os.path.exists(dir_name):
            os.makedirs(dir_name) #создаём папку со статьями за нужный год и месяц, если её ещё нет 

        article_number = str(len(os.listdir(dir_name)) + 1) #присваиваем статье номер в этой папке
                         
        req = urllib.request.Request('http://unecha-gazeta.ru/' + link)
        with urllib.request.urlopen(req) as response:
            my_html = response.read().decode('utf-8') #записываем в переменную html-код по ссылке

        file_path = dir_name + '\\' + article_number + '.txt' #путь к файлу, куда запищем html-код
        smaller_arr.append(file_path)
        
        f = open(file_path, 'w', encoding = 'utf-8')
        f.write(my_html)
        f.close() #записываем в файл html-код


        find_header = re.search('<h1>(.+)</h1>', my_html)
        header = find_header.group(1) #узнаём название статьи
        smaller_arr.append(header)

        created = day + '.' + month + '.' + year #дата создания статьи в нужном формате
        smaller_arr.append(created)

        find_topic = re.search('rel="category tag">(.+)</a>', my_html)
        topic = find_topic.group(1) #категория, к которой относится статья
        smaller_arr.append(topic)

        source = 'http://unecha-gazeta.ru/' + link #ссылка на страницу со статьей
        smaller_arr.append(source)

        mega_arr.append(smaller_arr)
        
    f1.write(file_path + '\t\t\t\t' + header + '\t' + created + '\tпублицистика\t\t\t' + topic +\
             '\t\tнейтральный\tн-возраст\tн-уровень\tрайонная\t' + source +\
             '\tУнечская газета\t\t'\
             + year + '\tгазета\tРоссия\tБрянская область\tru\n') #заполняем таблицу с метаданными

f1.close()


for root, dirs, files in os.walk('C:\\Users\\lilia\\Documents\\Unechskaya_gazeta\\plain'):
    for file in files:
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f2:
            text_f2 = f2.read()
            f2.close()
            pattern = re.compile(r'rel="category tag">(.+)</a> --></div>(\s)+<div class="clear10"></div>(.+?)<script async type="text/javascript">', re.DOTALL)
            #рег. выр. для куска html-кода, в котором содержтится текст статьи
            pre_result = re.search(pattern, text_f2) #находим кусок html-кода, в котором содержтится текст статьи
            almost_result = pre_result.group(3) #берем из этого куска собственно текст
            true_result = re.sub('<.*?>', '', almost_result) #чистим текст от тегов
            final_result = html.unescape(true_result) #отображаем правильно символы, которых нет на клавиатуре
        with open(os.path.join(root, file), 'w', encoding='utf-8') as f2:
            f2.write(final_result)
            f2.close()


for root, dirs, files in os.walk('C:\\Users\\lilia\\Documents\\Unechskaya_gazeta\\plain'):
    for file in files:
        xml_file = file.replace('txt', 'xml')
        xml_dir = root.replace('plain', 'mystem-xml')
        if not os.path.exists(xml_dir):
            os.makedirs(xml_dir)
        os.system(r'C:\\Users\\lilia\\Downloads\\mystem.exe' + r' -cid ' + root + os.sep + file + ' ' + xml_dir + os.sep + xml_file)
      #размечаем майстемом в формате xml

for root, dirs, files in os.walk('C:\\Users\\lilia\\Documents\\Unechskaya_gazeta\\plain'):
    for file in files:
        mystem_dir = root.replace('plain', 'mystem-plain')
        if not os.path.exists(mystem_dir):
            os.makedirs(mystem_dir)
        with open(mystem_dir + os.sep + file, 'w', encoding = 'utf-8') as f3:
            os.system(r'C:\\Users\\lilia\\Downloads\\mystem.exe' + r' -cid ' + root + os.sep + file + ' ' + mystem_dir + os.sep + file)
       #размечаем майстемом в формате txt


for i in range(len(mega_arr)):
    with open(mega_arr[i][0], 'r', encoding = 'utf-8') as file:
        text = file.read()

    with open(mega_arr[i][0], 'w', encoding = 'utf-8') as file:
        file.write('@au Noname\n')
        file.write('@ti ' + mega_arr[i][1] + '\n')
        file.write('@da ' + mega_arr[i][2] + '\n')
        file.write('@topic ' + mega_arr[i][3] + '\n')
        file.write('@url ' + mega_arr[i][4] + '\n')
        file.write(text) #добавляем к неразмеченным файлам метаданные


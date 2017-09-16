import urllib.request
import re

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        true_url = page.geturl() #итоговый url после переадресации
        true_url_1 = urllib.request.urlopen(true_url)
        text = true_url_1.read().decode('ISO-8859-1')
    except:
        text = ''
        return text
    # do something with the downloaded text

pages = []    

commonUrl = 'http://www.forumishqiptar.com/threads/54816'
commonUrl_1 = urllib.request.urlopen(commonUrl)
for i in range(1, 4):
    if i == 1:
        pageUrl = commonUrl_1.geturl()
    else:
        pageUrl = commonUrl_1.geturl() + 'page' + str(i)
    pages.append(download_page(pageUrl))

print(str(len(pages)))

for t in pages:
    clean_t = re.sub('<.*?>', '', t)
    clean_t = re.sub('<script>.*?</script>', '', clean_t)
    clean_t = re.sub('<!--.*?-->', '', clean_t)
    print(clean_t[:10])

 

import urllib.request
import json
import matplotlib
import matplotlib.pyplot as plt
import re

req = urllib.request.Request('https://api.vk.com/method/wall.get?\
owner_id=-1331201&count=101&v=5.74&\
access_token=3f696ad53f696ad53f696ad5c53f0be28233f693f696ad565b58e55581a24bf3bd34cc4') #выкачали 101 пост
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')


data = json.loads(result)

X = []
Y = []

dict_X_Y = {}


for i in range(len(data['response']['items'])): #цикл по нашим 101 посту
    x = 0 

    text_str = data['response']['items'][i]['text']
    len_words = len(text_str.split(' '))
    
    X.append(len_words) #складываем в массив длины постов в словах

    
    idx = data['response']['items'][i]['id']  #узнаём id поста
    req_2 = urllib.request.Request('https://api.vk.com/method/wall.getComments?\
owner_id=-1331201&post_id=' + str(idx) +'&preview_length=0&extended=1&count=100&v=5.74&\
access_token=3f696ad53f696ad53f696ad5c53f0be28233f693f696ad565b58e55581a24bf3bd34cc4') #выкачиваем комменты
    response_2 = urllib.request.urlopen(req_2)
    result_2 = response_2.read().decode('utf-8')
    data_2 = json.loads(result_2)


    
    for j in range(len(data_2['response']['profiles'])): #цикл по комментам к данному посту
        comm_str = data_2['response']['items'][j]['text'] 
        len_comm = len(comm_str.split(' '))
        x += len_comm #в этой переменной считаем сумму длин всех комментов к данному посту



    if len(data_2['response']['items']) != 0:
        Y.append(x / len(data_2['response']['items'])) #складываем в массив средние длины комментов к посту
    else:
        Y.append(0)


    
print(len(X))
print(len(Y))





#я не совсем поняла задание, поэтому на всякий случай рисую 2 графика

dict_help = {}
for k in X:
    if k not in dict_help:
        dict_help[k] = 1
    else:
        dict_help[k] += 1

dict_help_2 = {}
for l in range(len(X)):
    if X[l] not in dict_help_2:
        dict_help_2[X[l]] = Y[l]
    else:
        dict_help_2[X[l]] += Y[l]

for m in dict_help:
    dict_X_Y[m] = dict_help_2[m] / dict_help[m]

X_2 = []
Y_2 = []

for n in dict_X_Y:
    X_2.append(n)
    Y_2.append(dict_X_Y[n])



fig, ax = plt.subplots(nrows = 2, ncols = 1)
for s in range(len(X)):
    ax[0].scatter(X[s], Y[s], c = 'red')
for s in range(len(X_2)):
    ax[1].scatter(X_2[s], Y_2[s], c = 'red')

plt.show()



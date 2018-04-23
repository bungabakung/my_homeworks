import urllib.request
import json
import matplotlib
import matplotlib.pyplot as plt
import re

req = urllib.request.Request('https://api.vk.com/method/wall.get?\
owner_id=-102652602&count=500&extended=1&v=5.74&\
access_token=3f696ad53f696ad53f696ad5c53f0be28233f693f696ad565b58e55581a24bf3bd34cc4') #выкачали 101 пост
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')


data = json.loads(result)
#print(data)


Age = {}
City = {}
Age_num = {}
City_num = {}



for i in range(len(data['response']['profiles'])): #цикл по нашим 500 постам

    text_str = data['response']['items'][i]['text']
    len_words = len(text_str.split(' '))
    


    str_id = str(data['response']['profiles'][i]['id'])
    req_3 = urllib.request.Request('https://api.vk.com/method/users.get?\
user_ids=' + str_id + '&fields=bdate,city&v=5.74&\
access_token=3f696ad53f696ad53f696ad5c53f0be28233f693f696ad565b58e55581a24bf3bd34cc4')
#залезаем на страницу пользователя

    response_3 = urllib.request.urlopen(req_3)
    result_3 = response_3.read().decode('utf-8')
    data_3 = json.loads(result_3)


    if 'city' in data_3['response'][0]:
            
        if data_3['response'][0]['city']['id'] not in City:
            City[data_3['response'][0]['city']['id']] = len_words
        else:
            City[data_3['response'][0]['city']['id']] += len_words
                
        if data_3['response'][0]['city']['id'] not in City_num:
            City_num[data_3['response'][0]['city']['id']] = 1
        else:
            City_num[data_3['response'][0]['city']['id']] += 1


    if 'bdate' in data_3['response'][0]:

        r = re.search('[0-9][0-9]?\.[0-9][0-9]?\.([0-9][0-9][0-9][0-9])',\
                      data_3['response'][0]['bdate'])
        if r:
                
            if 2018 - int(r.group(1)) not in Age:
                Age[2018 - int(r.group(1))] = len_words
            else:
                Age[2018 - int(r.group(1))] += len_words


            if 2018 - int(r.group(1)) not in Age_num:
                Age_num[2018 - int(r.group(1))] = 1
            else:
                Age_num[2018 - int(r.group(1))] += 1

                


X_city = []
Y_city = []
X_age = []
Y_age = []

for x in City:
    X_city.append(x)
    Y_city.append(City[x] / City_num[x])

for y in Age:
    X_age.append(y)
    Y_age.append(Age[y] / Age_num[y])

fig, ax = plt.subplots(nrows = 2, ncols = 1)
for s in range(len(X_city)):
    ax[0].scatter(X_city[s], Y_city[s], c = 'blue')
for s in range(len(X_age)):
    ax[1].scatter(X_age[s], Y_age[s], c = 'green')


plt.show()

import urllib.request
import json
import os

req = urllib.request.Request('https://api.vk.com/method/wall.get?\
owner_id=-1331201&count=101&v=5.74&\
access_token=3f696ad53f696ad53f696ad5c53f0be28233f693f696ad565b58e55581a24bf3bd34cc4') #выкачали 101 пост
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')


data = json.loads(result)




for i in range(len(data['response']['items'])): #цикл по нашим 101 посту

    text_str = data['response']['items'][i]['text']
    

    
    idx = data['response']['items'][i]['id']  #узнаём id поста
    req_2 = urllib.request.Request('https://api.vk.com/method/wall.getComments?\
owner_id=-1331201&post_id=' + str(idx) +'&preview_length=0&extended=1&count=100&v=5.74&\
access_token=3f696ad53f696ad53f696ad5c53f0be28233f693f696ad565b58e55581a24bf3bd34cc4') #выкачиваем комменты
    response_2 = urllib.request.urlopen(req_2)
    result_2 = response_2.read().decode('utf-8')
    data_2 = json.loads(result_2)


    dir_name = 'C:\\Users\\lilia\\Documents\VK_matplotlib\\' + str(idx)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_path = dir_name + '\\post.txt'
    with open(file_path, 'w', encoding = 'utf-8') as f:
        f.write(text_str)
    
    for j in range(len(data_2['response']['items'])): #цикл по комментам к данному посту
        comm_str = data_2['response']['items'][j]['text'] 
        

        comm_path = dir_name + '\\' +\
                    str(data_2['response']['items'][j]['id']) +\
                    '.txt'
        with open(comm_path, 'w', encoding = 'utf-8') as f2:
            f2.write(comm_str)







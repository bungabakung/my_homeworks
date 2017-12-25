import os
import re
import json

di = {}
#print(str(len(os.listdir('thai_pages'))))
for k in os.listdir('thai_pages'):
    
    if os.path.isfile('thai_pages\\' + k):
        
        with open('thai_pages\\' + k, 'r', encoding = 'utf-8') as f:
            a = f.read()

            string2 = re.findall('(<tr><td class=th><a href=(.*?)>(.*?)</a></td>(.*?)\
<td class=pos>(.*?)</td><td>(.*?)</td></tr>)', a)
            for m in string2:

                y = m[2]
                y = re.sub('<(.*?)>', '', y)

                x = m[5]
                x = re.sub('<(.*?)>', '', x)
                x = re.sub('&#34;', '', x)
                x = re.sub('&#39;', '\'', x)

                di[m[2]] = x

#j = 0                
#for i in di:
    #if j < 5:
        #print(i)
        #print(di[i])
        #j += 1
    #else:
        #break
#print(str(len(di)))

arr1 = []
arr2 = []

for i in di:
    arr1.append(i)
    arr1.append(di[i])
    arr2.append(arr1)
    arr1 = []

json_string = json.dumps(arr2, ensure_ascii = False, indent = 4)
with open('di.json', 'w', encoding = 'utf-8') as f2:
    f2.write(json_string)

js = json.dumps(di, ensure_ascii = False, indent = 4)
with open('di_true.json', 'w', encoding = 'utf-8') as f4:
    f4.write(js)


di2 = {}
for i in di:
    if not di[i].endswith('.'):
        for x in di[i].split(';'):
            di2[x] = i
    else:
        di2[di[i]] = i
#print(str(len(di2)))

arr1 = []
arr2 = []

for i in di2:
    arr1.append(i)
    arr1.append(di2[i])
    arr2.append(arr1)
    arr1 = []

json_string_2 = json.dumps(arr2, ensure_ascii = False, indent = 4)
with open('di2.json', 'w', encoding = 'utf-8') as f3:
    f3.write(json_string_2)

js2 = json.dumps(di2, ensure_ascii = False, indent = 4)
with open('di2_true.json', 'w', encoding = 'utf-8') as f5:
    f5.write(js2)

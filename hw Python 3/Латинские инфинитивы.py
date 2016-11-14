arr=[]
s=input('Ввведите латинское слово ')
if len(s)!=0:
    arr.append(s)
while len(s)!=0:
    s=input('Ввведите латинское слово ')
    if s.endswith ('re') or s.endswith ('i')or s.endswith ('isse') \
    or s.endswith ('us esse') or s.endswith ('a esse') or s.endswith ('um esse') \
    or s.endswith ('um iri'):
        arr.append(s)
for i in range (len(arr)):
    print (arr[i])

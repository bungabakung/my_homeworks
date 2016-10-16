word=input('Введите русское существительное первого склонения')
if word.endswith('а') or word.endswith  ('я'):
    print ('Именительный падеж, единственное число')
elif word.endswith ('ами') or word.endswith ('ями'):
    print ('Творительный падеж, множественное число')
elif word.endswith('ы') or word.endswith  ('и'):
    print ('Родительный падеж, единственное число или именительный или винительный падеж, множественное число')
elif word.endswith('е'):
    print ('Дательный или предложный падеж, единственное число')
elif word.endswith('ой') or word.endswith ('ою') or  word.endswith('ёй') or word.endswith ('ёю')or word.endswith  ('ею') or word.endswith  ('ей'):
    print ('Творительный падеж, единственное число')
elif word.endswith('у') or  word.endswith('ю'):
    print ('Винительный падеж, единственное число')
elif word.endswith ('ам') or word.endswith  ('ям'):
    print ('Дательный падеж, множественное число')
elif word.endswith ('ах') or word.endswith('ях'):
    print ('Предложный падеж, множественное число')
else:
    print ('Родительный или винительный падеж, множественное число')

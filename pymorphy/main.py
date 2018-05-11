from pymorphy2 import MorphAnalyzer
import re
import random
import json
import flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

morph =  MorphAnalyzer()

app = Flask(__name__)

@app.route('/')

def start():
    
    if request.args.get('sentence'):
        s = request.args.get('sentence')
        #получаем введённое пользователем предложение

        s_arr = s.split()
        #делим предложения на слова

        st = '' #это строка, в которую мы потом запищем новое предложение

        with open ('file.json', 'r', encoding = 'utf-8') as f:
            a = f.read()
            b = json.loads(a)
            for word in s_arr:
                ana = morph.parse(word)
                first = ana[0]

                lemma = first.normalized
                t = str(lemma.tag)
    

                zamena = random.choice(b[t]) #это нужная нам лексема
                z = morph.parse(zamena)[0]


                if len(str(first.tag).split()) > 1:
                    tg = str(first.tag).split()[1] #это нужные нам характеристикт словоформы
                    m = set(tg.split(','))
                    try:
                        new = str(z.inflect(m).word)
                    except AttributeError:
                        new = zamena
                    st += new + ' '

                else:
                    st += zamena + ' '

        return render_template('res.html', y = st)
    return render_template('dz_4_2_start.html')


if __name__ == '__main__':
    app.run(debug = True)




    
        
    



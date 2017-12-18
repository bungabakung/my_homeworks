from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import sqlite3

#вот эта часть пока не работает
conn = sqlite3.connect('answers.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
#конец части, которая пока не работает


app = Flask(__name__)

@app.route('/')
def start():
    if request.args.get('answer1'):
        with open('answers1.txt', 'a', encoding = 'utf-8') as f:
            f.write('{}\n'.format(request.args.get('answer1')))
        return redirect(url_for('questions'))
    return render_template('project2.html')

@app.route('/questions')
def questions():
    if request.args.get('gender') and request.args.get('age'):
        with open('answers2.txt', 'a', encoding = 'utf-8') as f:
            f.write('{}\t{}\n'.format(request.args.get('gender'), request.args.get('age')))
        return('<h2>Спасибо за участие в опросе!</h2>')
    return render_template('project2_questions.html')

if __name__ == '__main__':
    app.run(debug = True)

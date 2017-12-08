from flask import Flask
from flask import request
from flask import render_template
from random import choice

app = Flask(__name__)

@app.route('/')
def hello():
    prizes = ['хомяка', 'автомобиль', 'деньги', 'сон']
    prize = choice(prizes)
    return render_template('new0.html', prize = prize)

@app.route('/steal')
def steal():
    number = request.args['number']

    f = open('cards.txt', 'a')
    f.write("{}\n".format(number))
    f.close()
    
    return '<h3>Спасибо!</h3>'

@app.route('/hi')
def hi():
    if 'name' in request.args:
        name = request.args['name']
        return '<html><body><h1>Hi, {}!</h1></body></html>'.format(name)
    else:
        return '<html><body><p>Введите имя</p></body></html>'

@app.route('/hell02')
def hello2():
    return '<html><body><h2>Hello, world!</h2></body></html>'

if __name__ == '__main__':
    app.run(debug=True)

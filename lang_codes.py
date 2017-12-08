from flask import Flask
from flask import request
from flask import render_template
import csv

app = Flask(__name__)


@app.route('/')
def langs():
    dict_langs = {}
    with open('lang_codes.csv', 'r', encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile)
    dict_langs = {row[0]: row[1] for row in reader}
    return render_template ('langs.html', langs = dict_langs)


@app.route('/langs')
@app.route('/langs/<letters>')
def lang_letters(letters = None):
    if letters is None:
        return '<html><body><h1>Введите, пожалуйста, буквы, с которых \
должны начинаться коды языков</h1></body></html>'
    else:
        dict_lang_letters = {}
        with open('lang_codes.csv', 'r', encoding = 'utf-8') as csvfile:
            reader = csv.reader(csvfile)
            dict_lang_letters = {row[0]: row[1] for row in reader if row[1].startswith(letters)}
        if len(dict_lang_letters) > 0:
            return render_template('lang_letters.html', langs = dict_lang_letters, letters = letters)
        elif len(dict_lang_letters) == 0:
            return '<html><body><h1>Языков, коды которых так начинаются, нет</h1></body></html>'


if __name__ == '__main__':
    app.run(debug=True)

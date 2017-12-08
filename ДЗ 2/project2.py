from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import sqlite3
import json
import csv




app = Flask(__name__)



@app.route('/')
def start():
    if request.args.get('answer1') and request.args.get('gender') and request.args.get('age'):
        with open('answers.csv', 'a', encoding = 'utf-8', newline = "") as file:
            arr = []
            arr.append([request.args.get('answer1'), request.args.get('gender'), request.args.get('age')])
            writer = csv.writer(file)
            writer.writerow(arr[0])
        return '<h2>Спасибо за участие в опросе!</h2>'
    return render_template('project2.html')


@app.route('/stats')
def stats():
    with open('answers.csv', 'r', encoding = 'utf-8', newline = "") as file:
        reader = csv.reader(file)
        dicti_a = {} #то же самое про возраст вместо пола
        dicti_g = {} #ключ -- пара ответ+пол, значение -- кол-во таких пар
        for row in reader:
            
            if (row[0], row[1]) not in dicti_g:
                dicti_g[(row[0], row[1])] = 1
            else:
                dicti_g[(row[0], row[1])] += 1
            if (row[0], row[2]) not in dicti_a:
                dicti_a[(row[0], row[2])] = 1
            else:
                dicti_a[(row[0], row[2])] += 1
    
            
        arr_g = [] #0 -- овет, 2 -- пол, 3 -- количество
        for i in dicti_g:
            arr_g.append([i[0], i[1], dicti_g[i]])
        len_g = len(arr_g)

        arr_a = []
        for j in dicti_a:
            arr_a.append([j[0], j[1], dicti_a[j]])                 
        len_a = len(arr_a)

    x = 0
    y = 0
    return render_template('project2_stats.html', arr_g = arr_g, arr_a = arr_a, len_g = len_g, len_a = len_a)

@app.route('/json')
def json1():
    with open('answers.csv', 'r', encoding = 'utf-8', newline = "") as file:
        reader = csv.reader(file)
        arr1 = []
        for row in reader:
            arr1.append(row)
        json_string = json.dumps(arr1, ensure_ascii = False, indent = 4)
    return json_string


@app.route('/search')
def search():
    if request.args.get('answer1'):
        with open('answer_search.txt', 'w', encoding = 'utf-8') as f:
            f.write(request.args.get('answer1'))

        return redirect(url_for('results', param = 'answer1', val_param = request.args.get('answer1')))
    if request.args.get('age'):
        with open('age_search.txt', 'w', encoding = 'utf-8') as f:
            f.write(request.args.get('age'))
 
        return redirect(url_for('results', param = 'age', val_param = request.args.get('age')))
    
    return render_template('project2_search.html')

@app.route('/results/<param>/<val_param>')
def results(param, val_param):

    with open('answers.csv', 'r', encoding = 'utf-8', newline = "") as file:
        reader = csv.reader(file)

        if param == 'answer1':   
            with open('answer_search.txt', 'r', encoding = 'utf-8') as f:
                a = f.read()
            results_arr = []
            for row in reader:
                if row[0] == a:
                    results_arr.append(row)
        
        if param == 'age':
            with open('age_search.txt', 'r', encoding = 'utf-8') as f:
                a = f.read()
            results_arr = []
            for row in reader:
                if row[2] == a:
                    results_arr.append(row)

    l = len(results_arr)
    i = 0
    return render_template('project2_results.html', results_arr = results_arr, l = l)

    
    

if __name__ == '__main__':
    app.run(debug = True)

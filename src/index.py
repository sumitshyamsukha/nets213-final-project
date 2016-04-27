#!/usr/local/opt/python/bin/python-2.7
from flask import Flask, render_template, request
import pickle
import operator
import urllib2
import json
from math import sqrt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/",  methods=['POST'])
def index_post():
    text = request.form['text']
    with open('test.txt', 'a') as f:
        f.write("\n"+text+"\n")
    return render_template('thanks.html')

@app.route('/comments')
def comments():
    comments = []
    with open('test.txt', 'r') as f:
        for line in f:
            if line != '' and line is not None and len(line) > 1:
                comments.append(line)
    return render_template('/comments.html', comments=comments)

@app.route('/comments', methods=['POST'])
def comments_post():
    comments = []
    try:
        pkl_file = open("ratings.pkl", "rb")
        ratings = pickle.load(pkl_file)
        pkl_file.close()
    except:
        ratings = {}
    with open('test.txt', 'r') as f:
        for line in f:
            if line != '' and line is not None and len(line) > 1:
                comments.append(line.strip())
    for i in request.form:
        if i.strip() in comments:
            if i.strip() in ratings:
                ratings[i.strip()].append(request.form[i])
            else:
                ratings[i.strip()] = [request.form[i]]

    output = open('ratings.pkl', 'wb')
    pickle.dump(ratings, output)
    output.close()
    return render_template('thanks.html')

@app.route('/ratings')
def ratings():
    try:
        pkl_file = open("ratings.pkl", "rb")
        ratings = pickle.load(pkl_file)
        pkl_file.close()
    except:
        ratings = {}
    confidence = []
    for i in ratings:
        u = 0
        d = 0
        for j in ratings[i]:
            if 'up' in j:
                u = u + 1
            if 'down' in j:
                d = d + 1
        confidence.append((i, _confidence(u, d)))
    sorted_ratings = sorted(confidence, key=operator.itemgetter(1), reverse=True)
    return render_template('/ratings.html', ratings=sorted_ratings)

# Source: http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
def _confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.96 #1.44 = 85%, 1.96 = 95%
    phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))

@app.route("/pdfview")
@app.route('/pdfview/<name>')
def pdfview(name=None):
    return render_template('/pdfview.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
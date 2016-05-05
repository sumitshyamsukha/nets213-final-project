#!/usr/local/opt/python/bin/python-2.7
from flask import Flask, render_template, request
import pickle
import operator
import urllib2
import json
import sys
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

@app.route('/user_submit')
def comments():
    comments = []
    with open('test.txt', 'r') as f:
        for line in f:
            if line != '' and line is not None and len(line) > 1:
                comments.append(line)
    return render_template('/user_submit.html', comments=comments)

@app.route('/user_submit', methods=['POST'])
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

@app.route('/view_users')
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
    return render_template('/view_users.html', ratings=sorted_ratings)

# Source: http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
def _confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.96 #1.44 = 85%, 1.96 = 95%
    phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))


def _get_comments(user) :
  try:
    request = urllib2.Request(construct_api_call(user), headers={
      'Authorization': 'Bearer ' + '6879-6446b8b4f00a2ecb7744e4c4fa211ff8'
      })
    text = urllib2.urlopen(request)
  except urllib2.HTTPError:
    sys.stderr.write('BAD REQUEST\n')
    return None
  try:
    response = json.loads(text.read())
  except ValueError:
    sys.stderr.write('JSON ERROR\n')
    return None
  comments = []
  for row in response['rows']:
    text = row['text'].strip()
    target = row['target']
    exact = 'null'
    for item in target:
        if 'selector' in item:
            for selector in item['selector']:
                if 'exact' in selector:
                    exact = selector['exact']
                    break
    if text != None and text != '':
      comments.append((exact.strip().encode('utf-8'), text.encode('utf-8')))
  return comments

def construct_api_call(user):
  return 'https://hypothes.is/api/search?limit=1000&user=' + str(user)

@app.route('/view_comments')
def get_comments():
  users = []
  corpus = {}
  with open('test.txt', 'r') as f:
    while True:
      user = f.readline().encode('utf-8')
      if user == '':
        break
      if user not in users:
        users.append(user)
  for user in users:
    if user not in corpus:
      corpus[user] = _get_comments(user)
  try:
    pkl_file = open("comment_ratings.pkl", "rb")
    ratings = pickle.load(pkl_file)
    pkl_file.close()
  except:
    ratings = {}
  return render_template('/view_comments.html', comments = corpus, rating = ratings)

@app.route('/user_comment')
def submit_comments():
  users = []
  corpus = {}
  with open('test.txt', 'r') as f:
    while True:
      user = f.readline().encode('utf-8')
      if user == '':
        break
      if user not in users:
        users.append(user)
  for user in users:
    if user not in corpus:
      corpus[user] = _get_comments(user)
  return render_template('/user_comment.html', comments = corpus)

@app.route('/user_comment', methods=['POST'])
def submit_comment_ratings():
  try:
    pkl_file = open("comment_ratings.pkl", "rb")
    ratings = pickle.load(pkl_file)
    pkl_file.close()
  except:
    ratings = {}
  for i in request.form:
    if i.strip() in ratings:
        if 'up' in request.form[i]:
            ratings[i.strip()]['up'] = ratings[i.strip()]['up'] + 1
        if 'down' in request.form[i]:
            ratings[i.strip()]['down'] = ratings[i.strip()]['down'] + 1
    else:
        if 'up' in request.form[i]:
            ratings[i.strip()] = {'up': 1}
        if 'down' in request.form[i]:
            ratings[i.strip()] = {'down': 1}
  print ratings
  output = open('comment_ratings.pkl', 'wb')
  pickle.dump(ratings, output)
  output.close()
  return render_template('thanks.html')

@app.route("/pdfview")
@app.route('/pdfview/<name>')
def pdfview(name=None):
    return render_template('/pdfview.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
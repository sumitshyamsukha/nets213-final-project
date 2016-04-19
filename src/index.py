#!/usr/local/opt/python/bin/python-2.7
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/",  methods=['POST'])
def index_post():
    text = request.form['text']
    with open('test.txt', 'a') as f:
        f.write("\n"+text+"\n")
    return "Thank you! Click the back button to go back!"

@app.route('/comments')
def comments():
    comments = []
    with open('test.txt', 'r') as f:
        for line in f:
            if line != '' and line is not None and len(line) > 1:
                comments.append(line)
    return render_template('/comments.html', comments=comments)

@app.route("/pdfview")
@app.route('/pdfview/<name>')
def pdfview(name=None):
    return render_template('/pdfview.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
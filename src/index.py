#!/usr/local/opt/python/bin/python-2.7
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('/index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
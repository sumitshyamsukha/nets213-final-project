#!/usr/local/opt/python/bin/python-2.7
from flask import Flask, Blueprint, render_template, abort

app = Flask(__name__)
store = Blueprint('annotator_store', )

@app.route("/")
def index():
    return "Hi"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('/index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
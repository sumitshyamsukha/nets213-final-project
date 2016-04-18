#!/usr/local/opt/python/bin/python-2.7
from flask import Flask, Blueprint, render_template, abort

app = Flask(__name__)
store = Blueprint('annotator_store', __name__)
app.register_blueprint(store, url_prefix='/lib/annotator-store')


@store.route('/store', methods=['GET'])
def store():
	return "hello world"

@app.route("/")
def index():
    return "Hi"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('/index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
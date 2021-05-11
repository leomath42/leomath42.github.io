#!/usr/bin/env python3
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path>/')
def post(path):
    page = path
    return render_template('post.html', page=page)


if __name__ == '__main__':
    app.run(port=5000)

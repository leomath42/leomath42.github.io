#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask_frozen import Freezer
from flask_flatpages import FlatPages
import sys


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_DEBUG'] = 1
pages = FlatPages(app)
FLATPAGES_EXTENSION = '.md'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path>/')
def post(path):
    page = path
    # return pages.get("foo")
    return pages.get('foo').html
    # return render_template('post.html', page=page)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        freezer = Freezer(app)
        freezer.freeze()
    else:
        app.run(port=5000, debug=True)


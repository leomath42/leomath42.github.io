#!/usr/bin/env python3
from flask import Flask
from flask import url_for
from flask import render_template
from flask import Response
from flask_frozen import Freezer
from flask_flatpages import FlatPages
from flask_flatpages import pygmented_markdown 
from werkzeug.exceptions import NotFound
from markupsafe import Markup

import sys


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_DEBUG'] = 1
app.config['FREEZER_RELATIVE_URLS']= False#True
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*']
pages = FlatPages(app)

FLATPAGES_EXTENSION = '.md'
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html', page=pages.get("index"))


########
# pages.reload()
def getPosts(pages):
    posts = []
    for page in list(pages).copy():
        if page.path.startswith('post'):
            page.path = page.path[5:]
            posts.append(page)

    return posts
########

@app.route('/blog/')
def blog():
    posts = getPosts(pages) 
    # posts=list(pages).copy()
    page_size = 4 
    n_post = len(posts)
    n_page = (len(posts) // page_size)
    n_page = n_page + 1 if (len(posts) / page_size) - n_page > 0 else n_page
    
    return Response(response=render_template('blog.html',page=pages.get("blog"),
        posts=posts, n_page=n_page, page_size=page_size, markup=Markup), mimetype="html")

@app.route('/project/')
def project():
    return render_template('project.html', page=pages.get("project")) 

@app.route('/<path:path>/')
def post(path):
    page = path
    return render_template('post.html', page=pages.get_or_404("post/{0}".format(page)))

@app.errorhandler(NotFound)
def notFound(e):
    return render_template('notFound.html')

@freezer.register_generator
def notFound():
    yield "/404.html"

@freezer.register_generator
def post():
    for page in set(pages):
        if page.path.startswith('post'):
            yield {'path' : page.path[5:]}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "test":
        freezer.run(debug=True)
    else:
        app.run(port=5000, debug=True)

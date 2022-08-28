#!/usr/bin/env python3
from flask import Flask, render_template
from flask import render_template_string
from flask import Response
from flask_frozen import Freezer
from flask_flatpages import FlatPages
from werkzeug.exceptions import NotFound
from flask_flatpages.utils import pygmented_markdown
from flask_flatpages import pygments_style_defs
import sys
from markupsafe import Markup


def my_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body, pages)


app = Flask(__name__)
pages = FlatPages()
freezer = Freezer()
app.config.from_pyfile("config.cfg")
app.config["FLATPAGES_HTML_RENDERER"] = my_renderer
pages.init_app(app)
freezer.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", page=pages.get("index"))


@app.route("/pygments.css")
def pygments_css():
    return pygments_style_defs("dracula"), 200, {"Content-Type": "text/css"}


def getPosts(pages):
    posts = []
    for page in list(pages):
        if page.path.startswith("post"):
            page.path = page.path[5:]
            posts.append(page)
    return posts


@app.route("/blog/")
def blog():
    posts = getPosts(pages)
    page_size = 4
    n_page = len(posts) // page_size
    n_page = n_page + 1 if (len(posts) / page_size) - n_page > 0 else n_page

    return Response(
        response=render_template(
            "blog.html",
            page=pages.get("blog"),
            posts=posts,
            n_page=n_page,
            page_size=page_size,
            markup=Markup,
        ),
        mimetype="html",
    )


@app.route("/project/")
def project():
    return render_template("project.html", page=pages.get("project"))


@app.route("/<path:path>/")
def post(path):
    formated = "post/{0}".format(path)
    return render_template("post.html", page=pages.get_or_404(formated))


@app.errorhandler(NotFound)
def notFound(e):
    return render_template("notFound.html")


@freezer.register_generator
def notFound_freezer():
    yield "/404.html"


@freezer.register_generator
def post_freezer():
    for page in set(pages):
        if page.path.startswith("post"):
            yield {"path": page.path[5:]}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "test":
        freezer.run(debug=True)
    else:
        app.run(port=5000, debug=True)

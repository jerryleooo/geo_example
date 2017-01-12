# -*- coding: utf-8 -*-

from flask import Flask
from geo_example.views import index


def create_app():
    app = Flask("geo_example")
    register_views(app)
    return app

def register_views(app):
    app.add_url_rule("/", "index", index, methods=["GET", "POST"])

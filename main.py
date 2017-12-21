#!/usr/bin/python3
# -*- coding: utf-8 -*-


import view
from app import app, db
from search.blueprint import search

app.register_blueprint(search, url_prefix='/search')

if __name__=='__main__':
    app.run()

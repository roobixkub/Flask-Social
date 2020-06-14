# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:48:02 2020

@author: Nate
"""


from flask import Flask, g

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.database
    g.db.connect()
    

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response






if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
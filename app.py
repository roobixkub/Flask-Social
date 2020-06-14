# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:48:02 2020

@author: Nate
"""


from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask_login import LoginManager

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'asdlfk a.zx .zjdf asjkdlfJFL:DSJFLASJ!#$sdefr'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None



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


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/')
def index():
    return 'Hey'

if __name__ == '__main__':
    models.initialize()
    models.User.create_user(
        name='natepease',
        email='nathanielpease@gmail.com',
        password='password',
        admin=True
    )
    app.run(debug=DEBUG, host=HOST, port=PORT)
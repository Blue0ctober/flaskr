# IMPORT ALL THE THINGS!
from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# CONFIG ALL THE THINGS!
DATABASE = 'tmp/flaskr.db'
DEBUT = True
SECRET_KEY = 'secret stuff'
USERNAME = 'admin'
PASSWORD = 'default'

# App Starts NOW!
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()

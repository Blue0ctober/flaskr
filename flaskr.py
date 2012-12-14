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

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                  [request.form['title'], request.form['test']])
    g.db.commit()
    flash('Newentry was successfully posted')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()

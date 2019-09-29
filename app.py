import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, g

DATABASE = '/home/simeone/Documents/Blog/blog.db'
DEBUG = True
SECRET_KEY = 'secret key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
    sql = sqlite3.connect('/home/simeone/Documents/Blog/blog.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


app = Flask(__name__)


@app.route('/')
def show_entries():
    cur = db.execute('select title,text from entries order by id desc')
    entries = [dict (title = row[0], text = row [1]) for row in cur.fetchall ()]

    return render_template('show_entries.html, entries')

@app.route('/add', methods = ['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db.execute ('insert into entries (title,text) values(?,?)', [request.form['title'], request.form['text']])
    db.commit()
    flash ('New entry was successfully posted')

    return redirect( url_for('show_entries'))

if __name__ == '__main__':
    app.run()

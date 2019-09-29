import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

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

if __name__ == '__main__':
    app.run()

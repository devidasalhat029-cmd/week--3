import sqlite3
from flask import flask,render_template,request,redirect,url_for,flash


app =flask(__name__)
app.secret_key='linkkiwi2026'

def get_db():
    conn = sqlite3.connect('practice.db')
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISIS students (
                 id INTERGER PRIMARY KEY aUTOINCREMENT ,
                 name TEXT NOT NULL,
                 ))
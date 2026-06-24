import sqlite3
from flask import Flask,render_template,request,Flash
app=Flask(__name__)
app.secret_key="linkkiwi2026"

def get_db():
    """Database connection"""
    conn=sqlite3.connect('myproject.db')
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    """create table"""
    conn=get_db()
    conn.execute 
    {'''
                 CRETE TABLE IF NOT EXISTS score (
                 id INTERGER PRIMARY KEY AUTOINCREMENT,
                 name text not null,
                 age iNTERGER NOT NULL,
                 village text Not null,
                 watwr_level text DEFFALT 0
                 )
                   '''}

    conn.commit()
    conn.close()

if __name__=="__main__":
    init_db()
    app.run(debug=True)


    
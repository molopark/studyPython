from distutils.log import debug
import os
from urllib import request
from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/', method=['GET', 'POST'])
def index():
    if request.method == 'GET':
        conn = sqlite3.connect("test.db", isolation_level=None)
        c = conn.cursor()
        c.execute(" \
            select * from table1  \
        ")
        res = c.fetchall()
        return jsonify(res)

    if request.method == 'POST':
        conn = sqlite3.connect("test.db", isolation_level=None)
        c = conn.cursor()
        c.execute(" \
            insert into table1 values( 2, 'lee', '2001-01-01') \
        ")
        return

if __name__ == '__main__':
    app.run(debug==True)

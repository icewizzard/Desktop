"""
from flask import Flask, render_template, url_for, request
from flask_restful import Api, Resource
import pandas as pd
from sqlalchemy import create_engine, insert, update, delete
import os

app = Flask(__name__)
conn_str = "postgresql+psycopg2://yoni:yoni123@localhost:5432/bank"
conn_post = create_engine(conn_str)

@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5432))
    app.run(debug=True, host='0.0.0.0', port=port)
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
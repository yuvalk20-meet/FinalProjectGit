from UserDB.py import *
from flask import Flask,render_template,url_for,request

app=Flask(__name__)
app.config['SECRET_KEY'] = ' you-will-never-guess'

## LOGIN ROUTES###
@app.route('/login', methods=['POST'])
def login():
    user = check_username(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return ## RENDER THE NECCESSARY PAGE##
    else:
        return ## RENDER THE NECCESSARY PAGE##


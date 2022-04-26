import os
import time

from flask import Flask, render_template, request, redirect, url_for
from repair_app.db_connector import connect_to_db, execute

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    error = None
    success = None
    if request.method == 'POST':
        if request.form['email'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            success = "Password Reset Link Sent."
    return render_template('reset.html', error=error, success= success)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    success = None
    if request.method == 'POST':
        if request.form['email'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            success = "Password Reset Link Sent."
    return render_template('signup.html', error=error, success= success)

@app.route('/profile', methods=['GET', 'POST'])
def edit():
    error = None
    success = None
    if request.method == 'POST':
        if request.form['email'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            success = "Password Reset Link Sent."
    return render_template('profile.html', error=error, success= success)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    error = None
    success = None
    if request.method == 'POST':
        if request.form['email'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            success = "Password Reset Link Sent."
    return render_template('submit.html', error=error, success= success)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
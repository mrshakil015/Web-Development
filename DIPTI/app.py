from flask import Flask, render_template, redirect, request, url_for, jsonify
# import mysql.connector
# import random

app=Flask(__name__)

AUTHORIZED_PASSWORD = "shakil015"
AUTHORIZED_USER = "shakil015"

@app.route('/', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        admin_username = request.form['admin_username']
        admin_password = request.form['admin_password']
        print(admin_username)
        print(admin_password)

        if (admin_username == AUTHORIZED_USER) and (admin_password == AUTHORIZED_PASSWORD):
            print("It works")
            return redirect(url_for('home'))
        else:
            error_message = "Invalid admin credentials"
            return render_template('login.html', error_message=error_message)
    error_message = "Invalid admin credentials"
    return render_template('login.html', error_message=error_message)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('admindashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
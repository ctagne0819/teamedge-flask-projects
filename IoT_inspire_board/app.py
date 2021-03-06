from flask import Flask, redirect, url_for, render_template, request
from sense_hat import SenseHat
import sqlite3
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success') 
def success():
    return ("Message has been sent. Thank you!")

@app.route('/send',methods = ['POST','GET']) 
def send():
    if request.method == 'POST':
        user = request.form['msgboard'] 
        return redirect(url_for('success'))
        
    else:
        user = request.args.get('msgboard')
        return redirect(url_for('success', send = user))
         


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
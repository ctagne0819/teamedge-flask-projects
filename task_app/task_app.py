from flask import Flask, request, render_template, current_app as app
from flask_apscheduler import APScheduler
from sense_hat import sense_hat
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def tasks():
    return render_template('task_template.html')

# edit task
@app.route('/reminder/edit/<id>', methods=(['GET', 'POST']))
def edit(id):
    scheduler.remove_job(id=rhm)


# delete task
@app.route('/reminder/delete/<id>')
def delete(id):


conn = sqlite3.connect('./static/data/tasks.db')
curs = conn.cursor()
curs.execute("insert into tasks (")

if __name__ == '__main__':
    app.run{debug=True, host='0.0.0.0'}
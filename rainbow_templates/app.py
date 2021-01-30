from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return ("Welcome to Chelsea's Rainbow Project, Part 2")

@app.route('/red') 
def red():
    return render_template('styles.html', color = 'red')

@app.route('/orange')
def orange():
    return render_template('styles.html', color = 'orange')

@app.route('/yellow')
def yellow():
    return render_template('styles.html', color = 'yellow')

@app.route('/green')
def green():
    return render_template('styles.html', color = 'green')

@app.route('/blue')
def blue():
    return render_template('styles.html', color = 'blue')

@app.route('/purple')
def purple():
    return render_template('styles.html', color = 'purple')

@app.route('/rainbow')
def rainbow():
    colors = ['red','orange','yellow','green','blue','purple']
    return render_template('rainbow.html', color = colors)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
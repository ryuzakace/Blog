#from app directory app object of class flask
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : "Gilmour"}
    return render_template('index.html', title = 'Comfortably Numb', user = user)


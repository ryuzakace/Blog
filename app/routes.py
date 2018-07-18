#from app directory app object of class flask
from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : "Gilmour"}
    posts = [
        {
            'author': {'username': 'Gangadhar'},
            'body': 'Geeta Vishwas, mai hu Kilwish!'
        },
        {
            'author': {'username': 'Ronaldo'},
            'body': 'Juventus, I\'m coming!'
        }
    ]
    return render_template('index.html', title = 'Comfortably Numb', user = user, posts = posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)

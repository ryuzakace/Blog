#from app directory app object of class flask
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'I haaavee Comfortably Numb!!'


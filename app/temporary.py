from flask import Flask

app = Flask(__names__)
from app import routes

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

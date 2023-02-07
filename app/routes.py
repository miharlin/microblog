from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mia'}
    posts = [
        {
            'author': {'username': 'Mike'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Bill'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

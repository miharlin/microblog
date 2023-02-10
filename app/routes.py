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

@app.route('/songs')
def songs():
    user = {'username': 'Mia'}
    songs = [
        {
            'title': 'let it be',
            'artist': 'Beetles'
        },
        {
            'title': 'billy jean',
            'artist': 'Micheal Jackson'
        }
    ]
    return render_template('songs.html', title='songs', user=user, songs=songs)

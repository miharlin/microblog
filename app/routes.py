from flask import render_template,flash, redirect
from app import app
from app.forms import LoginForm, NotesForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    form = NotesForm()
    if form.validate_on_submit():
        flash('Note entered: {}').format(form.notes)
        return redirect('/index')
    return render_template('notes.html', title='Notes App', form=form)

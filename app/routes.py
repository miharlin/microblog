from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, NotesForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', posts=posts)

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    form = NotesForm()
    print('Running notes form')
    if form.validate_on_submit():
        print('Entered notes:', form.notes)
        flash('Note entered: {}'.format(form.notes))
        return redirect('/index')
    return render_template('notes.html', title='Notes App', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

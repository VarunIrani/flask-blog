from flask import flash, redirect, render_template, url_for

from flask_blog import app
from flask_blog.forms import LoginForm, RegistrationForm
from flask_blog.models import Post, User

# Dummy Data
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'Blog Post 1 Content',
        'date_posted': 'October 29, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Blog Post 2 Content',
        'date_posted': 'October 30, 2019'
    },
    {
        'author': 'Diana Smith',
        'title': 'Blog Post 3',
        'content': 'Blog Post 3 Content',
        'date_posted': 'November 30, 2019'
    }
]


@app.route('/')
def home():
    return render_template('home.html.jinja', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html.jinja', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html.jinja', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'varunirani@gmail.com' and form.password.data == 'pass@123':
            flash(f'Successful Login {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed!', 'danger')

    return render_template('login.html.jinja', title='Login', form=form)

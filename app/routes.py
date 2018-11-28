from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {'username':'Miguel'}
    return  render_template('index.html', title='Home', user=user)

@app.route("/notitle")
def notitle():
    return  render_template('index.html')

@app.route("/showposts")
def showposts():
    posts = [
            {
                'author': {'username': 'Suzane'},
                'body': 'This is my body'
            },
            {
                'author': {'username': 'Richard'},
                'body': 'See my muscles'
            }
            ]
    return render_template('posts.html', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login required for user {}, remember_me={}'.format(
            form.username, form.remember_me))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)

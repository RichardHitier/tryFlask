from flask import render_template
from app import app

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

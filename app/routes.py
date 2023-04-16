from app import app
from forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route("/")
@app.route("/index")
def index():
    user = {"name":"Rashid"}
    posts = [
        {
            "author":{"name":"Susan"},
            "body": "Hello, there. My name is susan and today we are going to talk about Tech."
        },
        {
            "author":{"name":"Zack"},
            "body": "Hello, there. My name is Zack and today we are going to talk about Economics."
        }

    ]    
    return render_template("index.html", user=user, title="Home", posts=posts)

@app.route("login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Welcome {form.username.data}")
        return redirect(url_for('index'))
    
    return render_template("login.html", form=form, title="login")
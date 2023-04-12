from app import app
from flask import render_template

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
from flask import Flask, render_template

app = Flask(__name__)

#localhost로 접속했을때
@app.route("/")
def index():
    return render_template("index.html")

#localhost/signup로 접속했을때
@app.route("/signup/")
def signup():
    return render_template("signup.html")

app.run(port="80")
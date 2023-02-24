from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def greeter(name):
    return f"Hello, {escape(name)}"
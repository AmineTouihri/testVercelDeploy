from flask import Flask





app=Flask(__name__)


@app.route("/")
def langPage():
    return "hello vercel",200
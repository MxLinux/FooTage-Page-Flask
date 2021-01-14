from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/", defaults={"active": None})
@app.route("/<active>")
def index(active):
    path = os.getcwd() + "\\static\\videos"
    print(path)
    files = os.listdir(path)
    return render_template("index.html", files=files, active=active)

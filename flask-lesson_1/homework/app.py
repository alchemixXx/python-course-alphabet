import os

from flask import Flask, request, render_template, jsonify, make_response, abort, url_for, session
from werkzeug.utils import secure_filename, redirect

from main.routes import main
from fruits.routes import fruits
from vegetables.routes import vegetables

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)

@app.route("/")
def home():
    return render_template("home.html", title="Main page")


if __name__ == "__main__":

    app.run(debug=True)
from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", title="Main page")
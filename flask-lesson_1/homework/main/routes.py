from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", title="Main page")


@main.route("/porn")
def porn():
    return redirect(url_for('main.punch'))


@main.route("/punch")
def punch():
    return render_template("punch.html", title='ALARM!')

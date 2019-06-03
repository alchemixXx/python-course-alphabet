from flask import Flask, current_app, Blueprint

main = Blueprint('main', __name__)


@main.route("/")

from flask import Blueprint, render_template, abort

handlers = Blueprint('handlers', __name__)


@handlers.route("/error_404")
def error_testing():
    abort(404, "You can't do that!")


@handlers.errorhandler(404)
def handler_404(error):
    return render_template("handler_404.html", title="Error 404. Sorry!", error=error)

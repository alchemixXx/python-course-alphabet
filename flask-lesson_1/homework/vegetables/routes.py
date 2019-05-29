from flask import Blueprint, render_template, url_for

vegetables = Blueprint('vegetables', __name__)

@vegetables.route("/vegetables")
def vegetables_func():
    return render_template('vegetables.html', title='Vegetables Page!')


vegetables_list = ['Carrot', 'Potato', 'Onion', 'Pumpkin']
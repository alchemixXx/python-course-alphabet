from flask import Blueprint, render_template, url_for

fruits = Blueprint('fruits', __name__)

@fruits.route('/fruits')
def fruit_func():
    return render_template("fruits.html", title='Fruits Page!')


fruits_list = ['Apple', 'Gava', 'Orange', 'Banana']

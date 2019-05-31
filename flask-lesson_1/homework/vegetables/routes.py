from flask import Blueprint, render_template, request, url_for

vegetables = Blueprint('vegetables', __name__)
vegetables_list = ['Carrot', 'Potato', 'Onion', 'Pumpkin']


@vegetables.route("/vegetables")
@vegetables.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables_func(value=None):
    if request.method == "POST":
        vegetables_list.append(value)
        return "Vegetable was added successfully"
    elif request.method == "DELETE":
        vegetables_list.remove(value)
        return "Vegetable was deleted successfully"
    else:
        return render_template('vegetables.html', title='Vegetables Page!', vegetables_list=vegetables_list)

from flask import Blueprint, render_template

vegetables = Blueprint('vegetables', __name__)
vegetables_list = ['Carrot', 'Potato', 'Onion', 'Pumpkin']


@vegetables.route("/vegetables")
@vegetables.route('/vegetables/<string:value>', methods=['GET'])
def vegetables_get_func():
    return render_template('vegetables.html', title='Vegetables Page!', vegetables_list=vegetables_list)


@vegetables.route('/vegetables/<string:value>', methods=['POST'])
def vegetables_post_func(value=None):
    vegetables_list.append(value)
    return "Vegetable was added successfully"


@vegetables.route('/vegetables/<string:value>', methods=['DELETE'])
def vegetables_del_func(value=None):
    vegetables_list.remove(value)
    return "Vegetable was deleted successfully"


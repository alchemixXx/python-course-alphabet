from flask import Blueprint, render_template

vegetables = Blueprint('vegetables', __name__)
vegetables_list = ['Carrot', 'Potato', 'Onion', 'Pumpkin']


@vegetables.route("/vegetables")
def vegetables_get_func():
    return render_template('vegetables.html', title='Vegetables Page!', vegetables_list=vegetables_list)


@vegetables.route('/vegetables/<string:vegetable_name>', methods=['GET'])
def vegetable(vegetable_name):
    try:
        vegetable_index = vegetables_list.index(vegetable_name)
        vegetable = vegetables_list[vegetable_index]
    except:
        return "Sorry, there is no suck kind of vegetable"
    return render_template('specific_vegetable.html', title='Specific Vegetable Page!', vegetable_name=vegetable)


@vegetables.route('/vegetables/', methods=['POST'])
def vegetables_post_func(value=None):
    vegetables_list.append(value)
    return "Vegetable was added successfully"


@vegetables.route('/vegetables/', methods=['DELETE'])
def vegetables_del_func(value=None):
    vegetables_list.remove(value)
    return "Vegetable was deleted successfully"

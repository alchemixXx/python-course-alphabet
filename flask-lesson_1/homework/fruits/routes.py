from flask import Blueprint, render_template, request, redirect

fruits = Blueprint('fruits', __name__)

fruits_list = ['Apple', 'Guava', 'Orange', 'Banana']


@fruits.route("/fruits")
def fruits_get_func():
    return render_template('fruits.html', title='Fruits Page!', fruits_list=fruits_list)


@fruits.route('/fruits/<string:fruit_name>', methods=['GET'])
def fruit(fruit_name):
    try:
        fruit_index = fruits_list.index(fruit_name)
        fruit = fruits_list[fruit_index]
    except:
        return "Sorry, there is no suck kind of fruit"
    return render_template('specific_fruit.html', title='Specific Fruit Page!', fruit_name=fruit)


@fruits.route('/fruits/', methods=['POST'])
def fruits_post_func(value=None):
    fruits_list.append(value)
    return "Fruit was added successfully"


@fruits.route('/fruits/', methods=['DELETE'])
def fruits_del_func(value=None):
    fruits_list.remove(value)
    return "Fruit was deleted successfully"

from flask import Blueprint, render_template, request, redirect

fruits = Blueprint('fruits', __name__)

fruits_list = ['Apple', 'Guava', 'Orange', 'Banana']


# @fruits.route('/fruits')
# @fruits.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
# def fruit_func(value=None):
#     if request.method == "POST":
#         fruits_list.append(value)
#         return "Fruit was added successfully"
#     elif request.method == "DELETE":
#         fruits_list.remove(value)
#         return "Fruit was deleted successfully"
#     else:
#         return render_template("fruits.html", title='Fruits Page!', fruit_list=fruits_list)



@fruits.route("/fruits")
@fruits.route('/fruits/<string:value>', methods=['GET'])
def fruits_get_func():
    return render_template('fruits.html', title='Fruts Page!', fruits_list=fruits_list)


@fruits.route('/fruits/<string:value>', methods=['POST'])
def fruits_post_func(value=None):
    fruits_list.append(value)
    return "Fruit was added successfully"


@fruits.route('/fruits/<string:value>', methods=['DELETE'])
def fruits_del_func(value=None):
    fruits_list.remove(value)
    return "Fruit was deleted successfully"
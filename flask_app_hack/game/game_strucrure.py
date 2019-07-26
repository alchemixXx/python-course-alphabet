from flask_restful import fields

game_structure = {
    'secret_number': fields.Integer,
    'attempt': fields.Integer,
    'range_from': fields.Integer,
    'range_to': fields.Integer,
    'password': fields.String,
    'players': fields.String,
}

game_parse = reqparse.RequestParser()
game_parse.add_argument('secret_number')
game_parse.add_argument('attempt')
game_parse.add_argument('range_from')
game_parse.add_argument('range_to')
game_parse.add_argument('password')

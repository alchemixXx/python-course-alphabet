from flask import session
from flask_restful import Resource, marshal_with

from db import db
# from utils import check_login
from models import Game
from .game_strucrure import game_structure
from .parser import game_parse

DEFAULT_NUMBER_OF_ATTEMPTS = 3
DEFALT_RANGE = [0, 10]


class GameResources(Resource):
    # method_decorators = [check_login]

    @marshal_with(game_structure)
    def get(self):
        return Game.query.all()

    @marshal_with(game_structure)
    def post(self):
        args = game_parse.parse_args()
        args['author_id'] = session.get('user_id')
        if not args.get("secret_number"):
            del args['secret_number']
        if not args.get('attempt'):
            args['attempt'] = DEFAULT_NUMBER_OF_ATTEMPTS
        if not args.get('range_from'):
            args['range_from'] = DEFALT_RANGE[0]
        if not args.get('range_from'):
            args['range_to'] = DEFALT_RANGE[1]
        if not args.get("password"):
            del args['password']

        new_game = Game(**args)

        db.session.add(new_game)
        db.session.commit()
        return new_game

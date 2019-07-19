from flask_restful import Resource

from models import Game


class GameResources(Resource):

    def get(self):
        return Game.query.all()

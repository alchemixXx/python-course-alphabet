from flask_restful import Resource
from flask_lesson_3.db import db


class CreateDB(Resource):

    def post(self):
        db.create_all()
        db.session.commit()
        return "ok"

from flask import Blueprint
from flask_restful import Api

from .routes import CreateDB

create_db = Blueprint('create_db', __name__)

create_db_api = Api(create_db)

create_db_api.add_resource(CreateDB, '/create_db')

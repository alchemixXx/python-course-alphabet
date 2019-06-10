from flask import Flask, blueprints, current_app
from config import run_config
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object(run_config())
api = Api(app)

class HelloRest(Resource):
    def get(self):
        return {"key": "value"}, 201, {"custom_header": "value"}

a = ["Apple", 'Amazon', 'Alphabet', "Microsoft"]

class Companies(Resource):
    def get(self):
        responce = dict()
        for i, elem in enumerate(a):
            responce[i+1]: elem
        return responce


api.add_resource(HelloRest, "/")
api.add_resource(Companies, "/companies")

if __name__ == "__main__":
    app.run(debug=True)


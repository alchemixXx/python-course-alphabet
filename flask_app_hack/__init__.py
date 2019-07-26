from game_app import app
from config import Config
from create_db import create_db
from db import db
from game import game


def run_app():
    app.config.from_object(Config)
    app.register_blueprint(create_db)
    app.register_blueprint(game)
    # app.register_blueprint(auth)
    db.init_app(app)
    return app


if __name__ == '__main__':
    run_app().run(debug=True)


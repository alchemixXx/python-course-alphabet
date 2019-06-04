from flask import Flask

from .main.routes import main
from .fruits.routes import fruits
from .vegetables.routes import vegetables
from .handlers.routes import handlers

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)
app.register_blueprint(handlers)
app.secret_key = 'd6a7dd5539ce23fc722be0e5190a1526'


if __name__ == "__main__":
    app.run(debug=True)

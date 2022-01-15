from flask import Flask
import models
from views import main


def create_app(config_file='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    models.init_db(app)
    models.create_db(app)

    app.register_blueprint(main)

    return app




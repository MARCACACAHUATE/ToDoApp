#Flask
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Blueprint
from .auth import auth

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)


    app.config.from_object(Config)

    #Registro del Blueprint "auth"
    app.register_blueprint(auth)

    return app, db
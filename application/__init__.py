from flask import Flask
from config import Config
from database import mysql
from application.sesion import sesion

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la extensión MySQL
    mysql.init_app(app)

    # Registrar los blueprints
    app.register_blueprint(sesion)

    return app

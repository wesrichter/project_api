from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config: str):
    app = Flask(__name__)
    app.config.from_object(f'config.{config}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
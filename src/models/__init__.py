from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config: str):
    app = Flask(__name__)
    app.config.from_object(f'config.{config}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    return app
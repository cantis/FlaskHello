import os

from dotenv import load_dotenv
from flask import Flask

from .extensions import db


def create_app() -> Flask:
    """Application factory to create and configure the Flask app."""
    load_dotenv()
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False") == "True"
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes.home import bp as home_bp

    app.register_blueprint(home_bp)

    return app

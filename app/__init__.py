from flask import Flask
from .extensions import db
from .models import orm_objects

# Import blueprints
from .main import main_bp
from .auth import auth_bp
from .cards import cards_bp
from .sets import sets_bp
from .practice import practice_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)

    # Auto update changes
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["DEBUG"] = True

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(cards_bp, url_prefix="/cards")
    app.register_blueprint(sets_bp, url_prefix="/sets")
    app.register_blueprint(practice_bp, url_prefix="/practice")

    return app

from flask import Blueprint

cards_bp = Blueprint("cards", __name__)

from . import routes

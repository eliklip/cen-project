from flask import Blueprint

sets_bp = Blueprint("sets", __name__)

from . import routes

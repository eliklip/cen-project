from flask import Blueprint

practice_bp = Blueprint("practice", __name__)

from . import routes

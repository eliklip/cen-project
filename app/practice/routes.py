from flask import jsonify
from . import practice_bp

@practice_bp.route("/")
def practice_home():
    return jsonify({"page": "Practice"})

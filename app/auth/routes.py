from flask import jsonify
from . import auth_bp

@auth_bp.route("/login")
def login():
    return jsonify({"page": "Login"})

@auth_bp.route("/signup")
def signup():
    return jsonify({"page": "Signup"})

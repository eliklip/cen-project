from flask import jsonify
from . import cards_bp

@cards_bp.route("/")
def cards_home():
    return jsonify({"page": "Cards"})

@cards_bp.route("/new")
def new_card():
    return jsonify({"page": "New Card"})

@cards_bp.route("/edit")
def edit_card():
    return jsonify({"page": "Edit Card"})

@cards_bp.route("/delete")
def delete_card():
    return jsonify({"page": "Delete Card"})

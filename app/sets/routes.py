from flask import jsonify
from . import sets_bp

@sets_bp.route("/")
def sets_home():
    return jsonify({"page": "Sets"})

@sets_bp.route("/new")
def new_set():
    return jsonify({"page": "New Set"})

@sets_bp.route("/edit")
def edit_set():
    return jsonify({"page": "Edit Set"})

@sets_bp.route("/delete")
def delete_set():
    return jsonify({"page": "Delete Set"})

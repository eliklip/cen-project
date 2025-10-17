from flask import render_template
from . import main_bp

@main_bp.route("/")
@main_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", page_title="Dashboard")

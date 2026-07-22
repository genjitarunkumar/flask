from flask import Blueprint, render_template
#for declaring file as a routing 

home_bp = Blueprint("home", __name__)

@home_bp.route("/home")
def home():
    return render_template("home.html", name="Python Programming")

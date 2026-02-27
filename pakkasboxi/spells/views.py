from flask_cors import CORS
from flask import Blueprint, render_template

blueprint = Blueprint("spells", __name__)
CORS(blueprint, resources={r"/api/*": {"origins": "*"}})

@blueprint.route("/spells/mage",methods=["GET", "POST"])
def load_mage_page():
    return render_template("spells/mage.html")

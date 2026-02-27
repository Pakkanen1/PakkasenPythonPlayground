from flask_cors import CORS
from flask import Blueprint, render_template

blueprint = Blueprint("spells", __name__)
CORS(blueprint, resources={r"/api/*": {"origins": "*"}})

@blueprint.route("/spells/mage",methods=["GET", "POST"])
def load_mage_page():
    return render_template("spells/mage.html")

@blueprint.route("/spells/sorcerer",methods=["GET", "POST"])
def load_sorcerer_page():
    return render_template("spells/sorcerer.html")

@blueprint.route("/spells/druid",methods=["GET", "POST"])
def load_druid_page():
    return render_template("spells/druid.html")

@blueprint.route("/spells/witch",methods=["GET", "POST"])
def load_witch_page():
    return render_template("spells/witch.html")

@blueprint.route("/spells/wizard",methods=["GET", "POST"])
def load_wizard_page():
    return render_template("spells/wizard.html")

@blueprint.route("/spells/priest",methods=["GET", "POST"])
def load_priest_page():
    return render_template("spells/priest.html")

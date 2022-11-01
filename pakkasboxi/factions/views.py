from flask import Blueprint

blueprint = Blueprint("factions", __name__)

@blueprint.route("/factions")
def load_factions_page():
    return "<p>Coming soon...</p>"

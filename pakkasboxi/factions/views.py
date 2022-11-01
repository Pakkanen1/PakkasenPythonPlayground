from flask import Blueprint
from .models import Faction, Character, CharacterToFactionReputation, FactionToFactionReputation

blueprint = Blueprint("factions", __name__)

@blueprint.route("/factions")
def load_factions_page():
    return "<p>Coming soon...</p>"

@blueprint.route("/api/factions/<int:faction_id>", methods=["GET"])
def get_faction(faction_id: int):
    faction: Faction = Faction.get_by_id(faction_id)
    return {
        "id": faction.id,
        "name": faction.name,
        "symbol": faction.symbol_filepath,
        "color": faction.hex_color,
        "created": faction.created_ts,
        "modified": faction.modified_ts
    }

@blueprint.route("/api/factions/<int:faction_id>/reputations", methods=["GET"])
def get_faction_reputations(faction_id: int):
    reputations = FactionToFactionReputation.get_by_column_value(column_name="faction_id", value=faction_id)
    return reputations

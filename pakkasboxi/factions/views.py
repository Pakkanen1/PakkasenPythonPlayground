from flask import Blueprint
from sqlalchemy.orm import Session
from pakkasboxi.database import engine
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
    reputations = []
    with Session(engine) as session:
        query_result = session.query(FactionToFactionReputation)\
            .where(FactionToFactionReputation.faction_id == faction_id)
        for row in query_result:
            reputations.append(row.to_dict())
        return reputations

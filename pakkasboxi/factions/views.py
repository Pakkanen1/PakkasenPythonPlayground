from flask import Blueprint
from sqlalchemy.orm import Session
from pakkasboxi.database import engine
from .models import Faction, Character, CharacterToFactionReputation, FactionToFactionReputation, City, Country

blueprint = Blueprint("factions", __name__)

############
# Factions #
############

@blueprint.route("/factionreputation")
def load_factions_page():
    return "<p>Coming soon...</p>"

@blueprint.route("/api/factions/<int:faction_id>", methods=["GET"])
def get_faction(faction_id: int):
    faction: Faction = Faction.get_by_id(faction_id)
    return faction.to_dict()

@blueprint.route("/api/factions/<int:faction_id>/reputations", methods=["GET"])
def get_faction_reputations(faction_id: int):
    with Session(engine) as session:
        query_result = session.query(FactionToFactionReputation)\
            .where(FactionToFactionReputation.faction_id == faction_id)
        return [row.to_dict() for row in query_result]

@blueprint.route("/api/factions/<int:faction_id>/with-reputations", methods=["GET"])
def get_faction_with_reputations(faction_id: int):
    faction = get_faction(faction_id)
    reputations = get_faction_reputations(faction_id)
    reputation_objects = []
    for r in reputations:
        obj = {
            "faction": get_faction(r["target_faction_id"]),
            "reputation": r["reputation_points"]
        }
        reputation_objects.append(obj)
    faction["reputations"] = reputation_objects
    return faction

@blueprint.route("/api/factions", methods=["GET"])
def get_all_factions():
    return [f.to_dict() for f in Faction.get_all()]

@blueprint.route("/api/factions/reputations", methods=["GET"])
def get_all_faction_reputations():
    return [r.to_dict() for r in FactionToFactionReputation.get_all()]

##############
# Characters #
##############

@blueprint.route("/api/characters/<int:character_id>", methods=["GET"])
def get_character(character_id: int):
    character: Character = Character.get_by_id(character_id)
    return character.to_dict()

@blueprint.route("/api/characters/<int:character_id>/reputations", methods=["GET"])
def get_character_reputations(character_id: int):
    with Session(engine) as session:
        query_result = session.query(CharacterToFactionReputation) \
            .where(CharacterToFactionReputation.character_id == character_id)
        return [row.to_dict() for row in query_result]

@blueprint.route("/api/characters/<int:character_id>/with-reputations", methods=["GET"])
def get_character_with_reputations(character_id: int):
    character = get_character(character_id)
    reputations = get_character_reputations(character_id)
    reputation_objects = []
    for r in reputations:
        obj = {
            "faction": get_faction(r["faction_id"]),
            "reputation": r["reputation_points"]
        }
        reputation_objects.append(obj)
    character["reputations"] = reputation_objects
    return character

@blueprint.route("/api/characters", methods=["GET"])
def get_all_characters():
    return [c.to_dict() for c in Character.get_all()]

@blueprint.route("/api/characters/reputations", methods=["GET"])
def get_all_character_reputations():
    return [r.to_dict() for r in CharacterToFactionReputation.get_all()]

##########
# Cities #
##########

@blueprint.route("/api/cities", methods=["GET"])
def get_all_cities():
    return [c.to_dict() for c in City.get_all()]

#############
# Countries #
#############

@blueprint.route("/api/countries", methods=["GET"])
def get_all_countries():
    return [c.to_dict() for c in Country.get_all()]

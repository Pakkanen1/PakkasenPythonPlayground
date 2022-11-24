from flask_cors import CORS
from flask import Blueprint, render_template, request
from sqlalchemy.orm import Session
from pakkasboxi.database import engine
from .models import Faction, Character, CharacterToFactionReputation, \
                    FactionToFactionReputation, City, Country, Campaign
from flask_jwt_extended import jwt_required

blueprint = Blueprint("factions", __name__)
CORS(blueprint, resources={r"/api/*": {"origins": "*"}})

############
# Factions #
############

@blueprint.route("/factionreputation")
def load_factions_page():
    return render_template("factionmonitor.html")

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

@blueprint.route("/api/factions/with-reputations", methods=["GET"])
def get_factions_with_reputations():
    faction_ids = Faction.get_all_ids()
    return [get_faction_with_reputations(f) for f in faction_ids]

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

#############
# Campaigns #
#############

@blueprint.route("/api/campaigns", methods=["GET"])
def get_all_campaigns():
    return [c.to_dict() for c in Campaign.get_all()]

@blueprint.route("/api/campaigns/<int:campaign_id>/characters", methods=["GET"])
def get_campaign_characters(campaign_id: int):
    with Session(engine) as s:
        characters = s.query(Character).where(Character.campaign_id == campaign_id)
    return [c.to_dict() for c in characters]

@blueprint.route("/api/campaigns/<int:campaign_id>/factions", methods=["GET"])
def get_campaign_factions(campaign_id: int):
    with Session(engine) as session:
        query_result = session.query(Faction)\
            .join(FactionToFactionReputation, Faction.id == FactionToFactionReputation.faction_id)\
            .where(FactionToFactionReputation.campaign_id == campaign_id)
        return [row.to_dict() for row in query_result]

@blueprint.route("/api/campaigns/<int:campaign_id>/characters-with-reputations", methods=["GET"])
def get_reputations_of_campaign_characters(campaign_id: int):
    characters = get_campaign_characters(campaign_id)
    return [get_character_with_reputations(c["id"]) for c in characters]

@blueprint.route("/api/campaigns/<int:campaign_id>/faction/<int:faction_id>/with-reputations", methods=["GET"])
def get_campaign_faction_with_reputations(campaign_id: int, faction_id: int):
    faction = get_faction(faction_id)
    reputations = _get_faction_reputations_by_campaign_id(faction_id, campaign_id)
    reputation_objects = []
    for r in reputations:
        obj = {
            "faction": get_faction(r["target_faction_id"]),
            "reputation": r["reputation_points"]
        }
        reputation_objects.append(obj)
    faction["reputations"] = reputation_objects
    return faction

@blueprint.route("/api/campaigns/<int:campaign_id>/factions-with-reputations", methods=["GET"])
def get_reputations_of_campaign_factions(campaign_id: int):
    factions = get_campaign_factions(campaign_id)
    return [get_campaign_faction_with_reputations(campaign_id, f["id"]) for f in factions]

def _get_faction_reputations_by_campaign_id(faction_id: int, campaign_id: int):
    with Session(engine) as session:
        query_result = session.query(FactionToFactionReputation)\
            .where(FactionToFactionReputation.campaign_id == campaign_id,
                   FactionToFactionReputation.faction_id == faction_id)
        return [row.to_dict() for row in query_result]

######################
# REPUTATION UPDATES #
######################

@blueprint.route("/api/character-reputation/update", methods=["PATCH"])
@jwt_required(refresh=True, locations=["headers"])
def update_character_reputation_with_faction():
    request_data = request.get_json()
    character_id = request_data["character_id"]
    faction_id = request_data["faction_id"]
    reputation_to_add = request_data["reputation_to_add"]
    return _update_character_reputation_to_database(character_id, faction_id, reputation_to_add)

def _update_character_reputation_to_database(character_id: int, faction_id: int, reputation_to_add: int):
    reputation = CharacterToFactionReputation.query.filter_by(character_id=character_id, faction_id=faction_id).first()
    if not reputation:
        return "404"
    reputation.update(reputation_points=(reputation.reputation_points + reputation_to_add))
    reputation.save()
    return reputation.to_dict()

@blueprint.route("/api/faction-reputation/update", methods=["PATCH"])
@jwt_required(refresh=True, locations=["headers"])
def update_faction_reputation_with_another_faction():
    request_data = request.get_json()
    faction_id = request_data["faction_id"]
    target_id = request_data["target_faction_id"]
    reputation_to_add = request_data["reputation_to_add"]
    return _update_faction_reputation_to_database(faction_id, target_id, reputation_to_add)

def _update_faction_reputation_to_database(faction_id: int, target_faction_id: int, reputation_to_add: int):
    reputation = FactionToFactionReputation.query.filter_by(
        faction_id=faction_id, target_faction_id=target_faction_id).first()
    if not reputation:
        return "404"
    reputation.update(reputation_points=(reputation.reputation_points + reputation_to_add))
    reputation.save()
    return reputation.to_dict()

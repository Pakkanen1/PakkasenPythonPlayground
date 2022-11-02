import datetime as dt
from sqlalchemy_serializer import SerializerMixin
from pakkasboxi.database import Column, Model, SurrogatePK, db, relationship

class Faction(SurrogatePK, Model, SerializerMixin):

    __tablename__ = "factions"
    serialize_only = ("id", "name", "symbol_filepath", "description", "hex_color")

    name = Column(db.String(255), unique=True, nullable=False)
    symbol_filepath = Column(db.String(255), nullable=False)
    description = Column(db.Text, nullable=True)
    hex_color = Column(db.String(7), nullable=False)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, name, symbol_filepath, description, hex_color, **kwargs):
        db.Model.__init__(self, name=name, symbol_filepath=symbol_filepath,
                          description=description, hex_color=hex_color, **kwargs)

class Character(SurrogatePK, Model, SerializerMixin):

    __tablename__ = "characters"
    serialize_only = ("id", "name", "description", "active", "npc", "hex_color")

    name = Column(db.String(255), unique=True, nullable=False)
    description = Column(db.Text, nullable=True)
    # if the character is dead or somehow "inactive" they will not be displayed in the UI
    active = Column(db.Boolean, default=True)
    npc = Column(db.Boolean, default=False)
    hex_color = Column(db.String(7), nullable=False)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, name, description, active, npc, hex_color, **kwargs):
        db.Model.__init__(self, name=name, description=description,
                          active=active, npc=npc, hex_color=hex_color, **kwargs)


class CharacterToFactionReputation(SurrogatePK, Model, SerializerMixin):

    __tablename__ = "charactertofactionreputations"
    serialize_only = ("id", "character_id", "faction_id", "reputation_points")

    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)
    character = relationship("Character", foreign_keys=[character_id])
    faction_id = db.Column(db.Integer, db.ForeignKey("factions.id"), nullable=False)
    faction = relationship("Faction", foreign_keys=[faction_id])
    reputation_points = db.Column(db.Integer, nullable=False)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, faction, character, reputation_points, **kwargs):
        db.Model.__init__(self, faction=faction, character=character, reputation_points=reputation_points, **kwargs)

class FactionToFactionReputation(SurrogatePK, Model, SerializerMixin):

    __tablename__ = "factiontofactionreputations"
    serialize_only = ("id", "faction_id", "target_faction_id", "reputation_points")

    faction_id = db.Column(db.Integer, db.ForeignKey("factions.id"), nullable=False)
    faction = relationship("Faction", foreign_keys=[faction_id])
    target_faction_id = db.Column(db.Integer, db.ForeignKey("factions.id"), nullable=False)
    target_faction = relationship("Faction", foreign_keys=[target_faction_id])
    reputation_points = db.Column(db.Integer, nullable=False)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, faction, target_faction, reputation_points, **kwargs):
        db.Model.__init__(self, faction=faction, target_faction=target_faction,
                          reputation_points=reputation_points, **kwargs)

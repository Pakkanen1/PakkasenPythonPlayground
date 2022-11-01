import datetime as dt
from pakkasboxi.database import Column, Model, SurrogatePK, db, reference_col, relationship

class Faction(SurrogatePK, Model):

    __tablename__ = "factions"
    name = Column(db.String(255), unique=True, nullable=False)
    symbol_filepath = Column(db.String(255), nullable=False)
    description = Column(db.Text, nullable=True)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, name, symbol_filepath, description, **kwargs):
        db.Model.__init__(self, name=name, symbol_filepath=symbol_filepath, description=description, **kwargs)


class Character(SurrogatePK, Model):

    __tablename__ = "characters"
    name = Column(db.String(255), unique=True, nullable=False)
    description = Column(db.Text, nullable=True)
    # if the character is dead or somehow "inactive" they will not be displayed in the UI
    active = Column(db.Boolean, default=True)
    npc = Column(db.Boolean, default=False)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, name, description, active, npc, **kwargs):
        db.Model.__init__(self, name=name, description=description, active=active, npc=npc, **kwargs)


class FactionReputation(SurrogatePK, Model):

    __tablename__ = "factionreputations"
    faction_id = db.Column(db.Integer, nullable=False)  # faction that has the reputation
    faction = relationship("Faction", backref=db.backref("factions"))
    related_faction_id = reference_col("factions", nullable=True)  # the faction that has given the reputation
    related_faction = relationship("Faction", backref=db.backref("factions"))
    character_id = db.Column(db.Integer, nullable=True)
    character = relationship("Character", backref=db.backref("characters"))
    reputation_points = db.Column(db.Integer, nullable=False)
    created_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    modified_ts = Column(db.DateTime, nullable=False, default=dt.datetime.now)

    def __init__(self, faction, related_faction, character, reputation_points, **kwargs):
        db.Model.__init__(self, faction=faction, related_faction=related_faction,
                          character=character, reputation_points=reputation_points, **kwargs)



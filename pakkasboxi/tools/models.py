from enum import Enum

class CycleType(Enum):
    TWO_PATHS = 1
    TWO_KEYS = 2
    HIDDEN_SHORTCUT = 3
    DANGEROUS_ROUTE = 4
    FORESHADOWING_LOOP = 5
    LOCK_AND_KEY_CYCLE = 6
    BLOCKED_RETREAT = 7
    MONSTER_PATROL = 8
    ALTERED_RETURN = 9
    FALSE_GOAL = 10
    SIMPLE_LOCK_AND_KEY = 11
    GAMBIT = 12

class Lock(Enum):
    LOCK_HARD = "Literal door lock and key."
    TERRAIN_OR_NPC_HARD = "Terrain feature (pedestal, altar, mechanism, etc.) or NPC and key item."
    IMPASSABLE_HAZARD_HARD = "Impassible environmental hazard or magical effect and means to pass or dispel."
    MONSTER_SOFT = "Powerful (but potentially passable) monster and means to slay or evade."
    TRAP_SOFT = "Lethal (but potentially passable) trap and means to disable or evade."
    PERILOUS_HAZARD_SOFT = "Perilous (but potentially passable) hazard and means to neutralize or evade."

class Barrier(Enum):
    PHYSICAL_BARRIER = "Physical barrier (droppig stone etc.) that appears behind the players after they pass."
    MAGICAL_BARRIER = "Magical barrier (wall of force etc.) that appears behind the players after they pass."
    ONE_WAY_PATH = "One-way path (portal, gate, etc.)"
    ONE_WAY_TRAP = "One-way trap (pit, chute, portal, etc.)"
    TRAP = "Very dangerous but possibly passable TRAP that appears behind the players after they pass."
    HAZARD = "Very dangerous but possibly passable HAZARD that appears behind the players after they pass."
    MONSTER = "Very dangerous but possibly passable MONSTER that appears behind the players after they pass."

class CyclicDungeon:
    def __init__(self, overall_cycle: CycleType, subcycles: list[dict]):
        self.overall_cycle = overall_cycle.name
        self.subcycles = subcycles

    def to_dict(self):
        return {'overall_cycle': self.overall_cycle, 'subcycles': self.subcycles}

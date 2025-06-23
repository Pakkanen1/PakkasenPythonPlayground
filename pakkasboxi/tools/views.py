import json
import random
from flask_cors import CORS
from .models import CyclicDungeon, CycleType, Lock, Barrier
from flask import Blueprint, render_template

blueprint = Blueprint("tools", __name__)
CORS(blueprint, resources={r"/api/*": {"origins": "*"}})

@blueprint.route("/tools/generate-cycles/<int:cycle_amount>")
def load_tools_page(cycle_amount: int):
    dungeon = get_cyclic_dungeon(cycle_amount)
    return render_template("tools.html", cyclic_dungeon=dungeon)

@blueprint.route("/api/tools/cyclic/<int:cycle_amount>", methods=["GET"])
def get_cyclic_dungeon(cycle_amount: int):
    subcycles = _generate_random_cycles(cycle_amount)
    dungeon = CyclicDungeon(
        overall_cycle=random.choice(list(CycleType)),
        subcycles=subcycles
    )
    return dungeon.to_dict()

def _generate_random_cycles(amount: int):
    cycles = []
    for i in range(amount):
        name, extra = _generate_cycle()
        obj = {
            "cycle_name": name,
            "info": extra
        }
        cycles.append(obj)
    return cycles

def _generate_cycle():
    cycle = random.choice(list(CycleType))
    match cycle:
        case CycleType.TWO_KEYS:
            lock1 = random.choice(list(Lock))
            lock2 = random.choice(list(Lock))
            return cycle.name, [lock1.value, lock2.value]
        case CycleType.FORESHADOWING_LOOP:
            barrier = random.choice(list(Barrier))
            return cycle.name, [barrier.value]
        case CycleType.LOCK_AND_KEY_CYCLE:
            lock = random.choice(list(Lock))
            return cycle.name, [lock.value]
        case CycleType.BLOCKED_RETREAT:
            barrier = random.choice(list(Barrier))
            return cycle.name, [barrier.value]
        case CycleType.SIMPLE_LOCK_AND_KEY:
            lock = random.choice(list(Lock))
            return cycle.name, [lock.value]
    return cycle.name, []

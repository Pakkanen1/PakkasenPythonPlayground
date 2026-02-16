import random
from flask_cors import CORS
from .models import CyclicDungeon, CycleType, Lock, Barrier, RandomTable, RandomTableDatabase
from flask import Blueprint, render_template, request

blueprint = Blueprint("tools", __name__)
CORS(blueprint, resources={r"/api/*": {"origins": "*"}})

@blueprint.route("/tools/generate-cycles", defaults={"cycle_amount": 0}, methods=["GET", "POST"])
@blueprint.route("/tools/generate-cycles/<int:cycle_amount>")
def load_tools_page(cycle_amount: int):
    if request.method == "POST":
        cycle_amount = int(request.form.get("cycles"))
    dungeon = get_cyclic_dungeon(cycle_amount)
    tables = get_random_table_database()
    return render_template("tools.html", cyclic_dungeon=dungeon, random_tables=tables)

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

@blueprint.route("/tools/random-tables/db", methods=["GET"])
def get_random_table_database() -> RandomTableDatabase:
    #filepath = "C:\\gitnation\\randomtables\\randomtables22.json"
    filepath = "/home/repa/randomtables2.json"
    return RandomTableDatabase(filepath)

@blueprint.route("/api/tools/random-tables/names", methods=["GET"])
def get_random_table_names():
    tables = get_random_table_database()
    d = dict(tables.data).keys()
    return {"names": list(d)}

@blueprint.route("/api/tools/random-tables/<string:table_name>", methods=["GET"])
def get_item_from_random_table(table_name: str):
    tables = get_random_table_database()
    target_table = tables[table_name]
    return {"result": random.choice(target_table)}


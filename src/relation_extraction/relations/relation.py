from dataclasses import dataclass

#чуть позже скорее всего пределается под что-то новое
#поэтому пока оставляю
@dataclass
class Relation:
    subject: str
    predicate: str
    object: str
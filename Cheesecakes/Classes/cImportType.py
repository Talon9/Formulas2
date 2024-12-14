from enum import Enum

class ImportType(Enum):
    Unknown: int = 0
    Formula: int = 1
    Ingredients: int = 2
    Directions: int = 3
    KV_Pair: int = 4
    Notes: int = 5
    Misc: int = 6
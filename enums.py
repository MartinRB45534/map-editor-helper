"""
Some useful enums
"""

from enum import StrEnum

class Tribes(StrEnum):
    AIMO = "aimo"
    BARDUR = "bardur"
    HOODRICK = "hoodrick"
    IMPERIUS = "imperius"
    KICKOO = "kickoo"
    LUXIDOOR = "luxidoor"
    OUMAJI = "oumaji"
    QUETZALI = "quetzali"
    VENGIR = "vengir"
    XINXI = "xinxi"
    YADAKK = "yadakk"
    ZEBASI = "zebasi"

class Resources(StrEnum):
    NONE = ""
    FRUIT = "fruit"
    CROP = "crop"
    GAME = "game"
    FISH = "fish"
    WHALE = "whale"
    STARFISH = "starfish"
    METAL = "metal"
    AQUACROP = "aquacrop"

class Improvements(StrEnum):
    NONE = ""
    CITY = "city"
    RUIN = "ruin"

class Terrains(StrEnum):
    OCEAN = "ocean"
    WATER = "water"
    FIELD = "field"
    FOREST = "forest"
    MOUNTAIN = "mountain"

tribes_dict = {
    Tribes.AIMO: 10,
    Tribes.BARDUR: 3,
    Tribes.HOODRICK: 6,
    Tribes.IMPERIUS: 2,
    Tribes.KICKOO: 5,
    Tribes.LUXIDOOR: 7,
    Tribes.OUMAJI: 4,
    Tribes.QUETZALI: 12,
    Tribes.VENGIR: 8,
    Tribes.XINXI: 1,
    Tribes.YADAKK: 14,
    Tribes.ZEBASI: 9,
}

climates_dict = {
    10: Tribes.AIMO,
    3: Tribes.BARDUR,
    6: Tribes.HOODRICK,
    2: Tribes.IMPERIUS,
    5: Tribes.KICKOO,
    7: Tribes.LUXIDOOR,
    4: Tribes.OUMAJI,
    12: Tribes.QUETZALI,
    8: Tribes.VENGIR,
    1: Tribes.XINXI,
    14: Tribes.YADAKK,
    9: Tribes.ZEBASI,
}

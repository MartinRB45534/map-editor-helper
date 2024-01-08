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
    Tribes.AIMO: 2,
    Tribes.BARDUR: 4,
    Tribes.HOODRICK: 6,
    Tribes.IMPERIUS: 7,
    Tribes.KICKOO: 8,
    Tribes.LUXIDOOR: 9,
    Tribes.OUMAJI: 10,
    Tribes.QUETZALI: 11,
    Tribes.VENGIR: 12,
    Tribes.XINXI: 13,
    Tribes.YADAKK: 14,
    Tribes.ZEBASI: 15,
}

climates_dict = {
    2: Tribes.AIMO,
    4: Tribes.BARDUR,
    6: Tribes.HOODRICK,
    7: Tribes.IMPERIUS,
    8: Tribes.KICKOO,
    9: Tribes.LUXIDOOR,
    10: Tribes.OUMAJI,
    11: Tribes.QUETZALI,
    12: Tribes.VENGIR,
    13: Tribes.XINXI,
    14: Tribes.YADAKK,
    15: Tribes.ZEBASI,
}
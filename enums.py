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
    FRUIT = "fruit"
    CROP = "crop"
    GAME = "game"
    FISH = "fish"
    WHALE = "whale"
    STARFISH = "starfish"
    METAL = "metal"
    AQUACROP = "aquacrop"
    NONE = ""

class Improvements(StrEnum):
    CITY = "city"
    RUIN = "ruin"
    NONE = ""

class Terrains(StrEnum):
    WATER = "water"
    OCEAN = "ocean"
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
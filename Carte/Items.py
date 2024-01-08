import os
import cv2 as cv #pylint: disable=import-error

TRIBUS = ["Ai-mo","Bardur","Hoodrick","Imperius","Kickoo","Luxidoor","Oumaji","Quetzali","Vengir","Xin-xi","Yadakk","Zebasi"]
UNITES_NAVALES = ["battleship","boat","navalon","ship"]
UNITES_TERRESTRES = ["archer","battle sled","catapult","defender","dragon egg","gaami","giant","ice archer","ice fortress","knight","mind bender","mooni","polytaur","rider","swordsman","warrior"]
UNITES_AMPHIBIES = ["amphibian","baby dragon","crab","fire dragon","tridention"]
UNITES = UNITES_NAVALES + UNITES_AMPHIBIES + UNITES_TERRESTRES
MONUMENTS = ["altar of peace","emperors tomb","eye of god","gate of power","grand bazaar","park of fortune","tower of wisdom"]
TERRAINS_G = ["Shallow water","Deep water"]
TERRAINS_S = ["forest","ground","mountain"]
RESOURCES_G = ["Crop","Fish","Metal","Whale","Ruin","Village"]
RESOURCES_S = ["fruit","game"]
ALL_BUILDINGS = RESOURCES_G + RESOURCES_S


ASSETS = {tribe:{
    sprite: {
        "image":
        cv.resize(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,"Units",tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED),(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,"Units",tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[0]//10,cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,"Units",tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[1]//10))
    if sprite in UNITES else
        cv.resize(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,"Monuments",tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED),(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,"Monuments",tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[0]//10,cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,"Monuments",tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[1]//10))
    if sprite in MONUMENTS else
        cv.resize(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Miscellaneous",sprite+".png")), cv.IMREAD_UNCHANGED),(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Miscellaneous",sprite+".png")), cv.IMREAD_UNCHANGED).shape[0]//10,cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Miscellaneous",sprite+".png")), cv.IMREAD_UNCHANGED).shape[1]//10))
    if sprite in TERRAINS_G else
        cv.resize(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED),(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[0]//10,cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[1]//10))
    if sprite in TERRAINS_S else
        cv.resize(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Miscellaneous",sprite+".png")), cv.IMREAD_UNCHANGED),(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Miscellaneous",sprite+".png")), cv.IMREAD_UNCHANGED).shape[0]//10,cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Miscellaneous",sprite+".png")), cv.IMREAD_UNCHANGED).shape[1]//10))
    if sprite in RESOURCES_G else
        cv.resize(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED),(cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[0]//10,cv.imread(os.path.abspath(os.path.join("Polytopia Sprites/Tribes",tribe,tribe+" "+sprite+".png")), cv.IMREAD_UNCHANGED).shape[1]//10))
    if sprite in RESOURCES_S else
        "",
        "shape":[1200,2000],
        "decalage":[0,0]}
    for sprite in UNITES+MONUMENTS+TERRAINS_G+TERRAINS_S+RESOURCES_G+RESOURCES_S
    } for tribe in TRIBUS}

for tribe in TRIBUS:
    for unit in UNITES:
        ASSETS[tribe][unit]["decalage"][0]=440
        ASSETS[tribe][unit]["decalage"][1]=-710

    ASSETS[tribe]["Shallow water"]["decalage"][1]=125
    ASSETS[tribe]["Deep water"]["decalage"][1]=125
    ASSETS[tribe]["Ruin"]["decalage"][0]=345
    ASSETS[tribe]["Ruin"]["decalage"][1]=-240

    ASSETS[tribe]["mountain"]["shape"] = [600,1000]
    ASSETS[tribe]["Metal"]["decalage"][0]=-45
    ASSETS[tribe]["Metal"]["decalage"][1]=-285

    ASSETS[tribe]["Fish"]["decalage"][0] = -30
    ASSETS[tribe]["Fish"]["decalage"][1] = -90

    ASSETS[tribe]["Whale"]["decalage"][0] = 30
    ASSETS[tribe]["Whale"]["decalage"][1] = -65

    ASSETS[tribe]["forest"]["decalage"][0]=-20
    ASSETS[tribe]["forest"]["decalage"][1]=-290

    ASSETS[tribe]["fruit"]["shape"] = [600,1000]

ASSETS["Ai-mo"]["mountain"]["decalage"][1]=-470
ASSETS["Bardur"]["mountain"]["decalage"][1]=-330
ASSETS["Hoodrick"]["mountain"]["decalage"][1]=0
ASSETS["Imperius"]["mountain"]["decalage"][1]=-345
ASSETS["Kickoo"]["mountain"]["decalage"][0]=-50
ASSETS["Kickoo"]["mountain"]["decalage"][1]=-290
ASSETS["Luxidoor"]["mountain"]["decalage"][1]=-340
ASSETS["Oumaji"]["mountain"]["decalage"][1]=-325
ASSETS["Quetzali"]["mountain"]["decalage"][0]=170
ASSETS["Quetzali"]["mountain"]["decalage"][1]=-295
ASSETS["Vengir"]["mountain"]["decalage"][1]=-400
ASSETS["Xin-xi"]["mountain"]["decalage"][1]=-470
ASSETS["Yadakk"]["mountain"]["decalage"][0]=-60
ASSETS["Yadakk"]["mountain"]["decalage"][1]=-515
ASSETS["Zebasi"]["mountain"]["decalage"][1]=-175

ASSETS["Ai-mo"]["game"]["shape"]=[600,1000]
ASSETS["Bardur"]["game"]["shape"]=[600,1000]
ASSETS["Hoodrick"]["game"]["shape"]=[600,1000]
ASSETS["Imperius"]["game"]["shape"]=[600,1000]
ASSETS["Kickoo"]["game"]["shape"]=[600,1000]
ASSETS["Luxidoor"]["game"]["shape"]=[600,1000]
ASSETS["Oumaji"]["game"]["shape"]=[600,1000]
ASSETS["Quetzali"]["game"]["shape"]=[600,1000]
ASSETS["Vengir"]["game"]["shape"]=[600,1000]
ASSETS["Xin-xi"]["game"]["shape"]=[600,1000]
ASSETS["Yadakk"]["game"]["shape"]=[1650,2750]
ASSETS["Zebasi"]["game"]["shape"]=[600,1000]

ASSETS["Ai-mo"]["game"]["decalage"][0]=830
ASSETS["Ai-mo"]["game"]["decalage"][1]=150
ASSETS["Bardur"]["game"]["decalage"][0]=830
ASSETS["Bardur"]["game"]["decalage"][1]=275
ASSETS["Hoodrick"]["game"]["decalage"][0]=790
ASSETS["Hoodrick"]["game"]["decalage"][1]=225
ASSETS["Imperius"]["game"]["decalage"][0]=830
ASSETS["Imperius"]["game"]["decalage"][1]=235
ASSETS["Kickoo"]["game"]["decalage"][0]=825
ASSETS["Kickoo"]["game"]["decalage"][1]=345
ASSETS["Luxidoor"]["game"]["decalage"][0]=805
ASSETS["Luxidoor"]["game"]["decalage"][1]=290
ASSETS["Oumaji"]["game"]["decalage"][0]=830
ASSETS["Oumaji"]["game"]["decalage"][1]=290
ASSETS["Quetzali"]["game"]["decalage"][0]=865
ASSETS["Quetzali"]["game"]["decalage"][1]=190
ASSETS["Vengir"]["game"]["decalage"][0]=700
ASSETS["Vengir"]["game"]["decalage"][1]=190
ASSETS["Xin-xi"]["game"]["decalage"][0]=830
ASSETS["Xin-xi"]["game"]["decalage"][1]=205
ASSETS["Yadakk"]["game"]["decalage"][0]=835
ASSETS["Yadakk"]["game"]["decalage"][1]=240
ASSETS["Zebasi"]["game"]["decalage"][0]=830
ASSETS["Zebasi"]["game"]["decalage"][1]=170

ASSETS["Ai-mo"]["fruit"]["decalage"][0]=640
ASSETS["Ai-mo"]["fruit"]["decalage"][1]=170
ASSETS["Bardur"]["fruit"]["decalage"][0]=500
ASSETS["Bardur"]["fruit"]["decalage"][1]=345
ASSETS["Hoodrick"]["fruit"]["decalage"][0]=585
ASSETS["Hoodrick"]["fruit"]["decalage"][1]=250
ASSETS["Imperius"]["fruit"]["decalage"][0]=520
ASSETS["Imperius"]["fruit"]["decalage"][1]=320
ASSETS["Kickoo"]["fruit"]["decalage"][0]=710
ASSETS["Kickoo"]["fruit"]["decalage"][1]=290
ASSETS["Luxidoor"]["fruit"]["decalage"][0]=520
ASSETS["Luxidoor"]["fruit"]["decalage"][1]=210
ASSETS["Oumaji"]["fruit"]["decalage"][0]=530
ASSETS["Oumaji"]["fruit"]["decalage"][1]=240
ASSETS["Quetzali"]["fruit"]["decalage"][0]=655
ASSETS["Quetzali"]["fruit"]["decalage"][1]=210
ASSETS["Vengir"]["fruit"]["decalage"][0]=710
ASSETS["Vengir"]["fruit"]["decalage"][1]=300
ASSETS["Xin-xi"]["fruit"]["decalage"][0]=500
ASSETS["Xin-xi"]["fruit"]["decalage"][1]=390
ASSETS["Yadakk"]["fruit"]["decalage"][0]=500
ASSETS["Yadakk"]["fruit"]["decalage"][1]=60
ASSETS["Zebasi"]["fruit"]["decalage"][0]=500
ASSETS["Zebasi"]["fruit"]["decalage"][1]=330

ASSETS_ = {}
for key, tribe in ASSETS.items():
    tribe_ = {}
    for sprite in tribe.values():
        for x in ["shape","decalage"]:
            for i in [0,1]:
                sprite[x][i]/=10
    tribe_["city"] = tribe["Village"]
    tribe_["ruin"] = tribe["Ruin"]
    tribe_["water"] = tribe["Shallow water"]
    tribe_["ocean"] = tribe["Deep water"]
    tribe_["field"] = tribe["ground"]
    tribe_["forest"] = tribe["forest"]
    tribe_["mountain"] = tribe["mountain"]
    tribe_["game"] = tribe["game"]
    tribe_["fruit"] = tribe["fruit"]
    tribe_["metal"] = tribe["Metal"]
    tribe_["starfish"] = tribe["ship"]
    tribe_["fish"] = tribe["Fish"]
    tribe_["crop"] = tribe["Crop"]
    tribe_["aquacrop"] = tribe["boat"]
    tribe_["whale"] = tribe["Whale"]
    ASSETS_[key] = tribe_


ASSETS_["aimo"] = ASSETS_["Ai-mo"]
ASSETS_["bardur"] = ASSETS_["Bardur"]
ASSETS_["hoodrick"] = ASSETS_["Hoodrick"]
ASSETS_["imperius"] = ASSETS_["Imperius"]
ASSETS_["kickoo"] = ASSETS_["Kickoo"]
ASSETS_["luxidoor"] = ASSETS_["Luxidoor"]
ASSETS_["oumaji"] = ASSETS_["Oumaji"]
ASSETS_["quetzali"] = ASSETS_["Quetzali"]
ASSETS_["vengir"] = ASSETS_["Vengir"]
ASSETS_["xinxi"] = ASSETS_["Xin-xi"]
ASSETS_["yadakk"] = ASSETS_["Yadakk"]
ASSETS_["zebasi"] = ASSETS_["Zebasi"]

ASSETS = ASSETS_

"""
Documentation de la classe Affichage
"""
from copy import copy

import numpy as np
import cv2 as cv #pylint: disable=import-error

from Carte.Items import ASSETS


def affiche(carte, tailles=[120,200], assets=ASSETS, tile_centers = None, marges = [0,0,0,0]):
    "Affiche"
    tailles = copy(tailles)
    background = np.full((int(tailles[0]*(len(carte)+6)),int(tailles[1]*(len(carte[0])+5)),4),0,np.uint8)
    background[:,:,3]=255
    if tile_centers is None :
        tile_centers = [[[int(tailles[1] * (j+len(carte)-i+3)/2),int(tailles[0] * (i+j+8)/2)]for j in range(len(carte[i]))]for i in range(len(carte))]
        background = np.full((int(tailles[0]*(len(carte)+6)),int(tailles[1]*(len(carte[0])+5)),4),0,np.uint8)
        background[:,:,3]=255
    else:
        background = np.full((int(max([tile_center[1] for ligne in tile_centers for tile_center in ligne]) + tailles[0]*3),int(max([tile_center[0] for ligne in tile_centers for tile_center in ligne]) + tailles[1]*3),4),0,np.uint8)
        background[:,:,3]=255
    for i, row in enumerate(carte):
        for j, tile in enumerate(row):
            for key in ["terrain","ressource","batiment"]:
                if tile[key] == "":
                    continue
                if tile[key] in ["forest", "mountain"]:
                    asset = assets[tile["tribu"]]["field"]
                    image = asset["image"]
                    shape = copy(asset["shape"])
                    decalage = copy(asset["decalage"])
                    overlay = copy(image)
                    B,G,R = copy(overlay[:,:,0]),copy(overlay[:,:,1]),copy(overlay[:,:,2])
                    overlay[:,:,0],overlay[:,:,1],overlay[:,:,2] = R,G,B
                    width,length = overlay.shape[:2]
                    size = (int((width*tailles[1])/shape[1]),int((length*tailles[0])/shape[0]))
                    overlay = cv.resize(overlay,size)
                    decalage = (int((decalage[0]*tailles[0])/120),int((decalage[1]*tailles[1])/200))
                    put4ChannelImageOn4ChannelImageNice(background, overlay, tile_centers[i][j][0] -100 + decalage[0], tile_centers[i][j][1] - 60 + decalage[1])
                asset = assets[tile["tribu"]][tile[key]]
                image = asset["image"]
                shape = copy(asset["shape"])
                decalage = copy(asset["decalage"])
                overlay = copy(image)
                B,G,R = copy(overlay[:,:,0]),copy(overlay[:,:,1]),copy(overlay[:,:,2])
                overlay[:,:,0],overlay[:,:,1],overlay[:,:,2] = R,G,B
                width,length = overlay.shape[:2]
                size = (int((width*tailles[1])/shape[1]),int((length*tailles[0])/shape[0]))
                overlay = cv.resize(overlay,size)
                decalage = (int((decalage[0]*tailles[0])/120),int((decalage[1]*tailles[1])/200))
                put4ChannelImageOn4ChannelImageNice(background, overlay, tile_centers[i][j][0] -100 + decalage[0], tile_centers[i][j][1] - 60 + decalage[1])
    return background[marges[0]:-1-marges[2],marges[1]:-1-marges[3]],tile_centers

def put4ChannelImageOn4ChannelImage(back, fore, x, y):
    rows, cols, _channels = fore.shape
    trans_indices = fore[...,3] != 0
    overlay_copy = back[y:y+rows, x:x+cols]
    try:
        overlay_copy[trans_indices] = fore[trans_indices]
    except Exception as e:
        print(x)
        print(x+cols)
        print(overlay_copy.shape)
        print(fore.shape)
        overlay_copy[trans_indices] = fore[trans_indices]
    back[y:y+rows, x:x+cols] = overlay_copy

def put4ChannelImageOn4ChannelImageNice(back, fore, x, y):
    rows, cols, _channels = fore.shape
    max_y, max_x, _channels_back = back.shape
    # print(x,y,rows,cols)
    if x<0:
        cols+=x
        fore = fore[:, -x:]
        x=0
    if x+cols>=max_x:
        cols = max_x-x
        fore = fore[:, :cols]
    if y<0:
        rows+=y
        fore = fore[-y:, :]
        y=0
    if y+rows>=max_y:
        rows = max_y-y
        fore = fore[:rows, :]
    trans_indices = fore[...,3] != 0
    overlay_copy = back[y:y+rows, x:x+cols]
    try:
        overlay_copy[:,:,:][trans_indices] = np.multiply((1-fore[:,:,3:][trans_indices]/255),overlay_copy[:,:,:][trans_indices]) + np.multiply((fore[:,:,3:][trans_indices])/255,fore[:,:,:][trans_indices])
    except Exception as e:
        print(y)
        print(y+cols)
        print(back.shape)
        print(overlay_copy.shape)
        print(fore.shape)
        overlay_copy[:,:,:][trans_indices] = np.multiply((1-fore[:,:,3:][trans_indices]/255),overlay_copy[:,:,:][trans_indices]) + np.multiply((fore[:,:,3:][trans_indices])/255,fore[:,:,:][trans_indices])
    back[y:y+rows, x:x+cols] = overlay_copy

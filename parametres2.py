"""
Une épidémie plus dangereuse
Changements:
    taux de mortalité plus élévé
    infectiosité moins grande
"""

LONG = 40
HAUT = 40
P0 = 10
P_INFECT = 10
TX_MORT = 20
NBS_J_IMM = 7
P_MASQUES = 90
P_MASQUES_MAL = 70
P_DEBUT_MASQUES = 40
P_INFECT_MASQUES = P_INFECT / 10
P_INFECT_MASQUES_MAL = P_INFECT / 2
NBS_J_INCUBATION = 4
NBS_J_GUER = 7 + NBS_J_INCUBATION
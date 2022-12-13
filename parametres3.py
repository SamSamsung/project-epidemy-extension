"""
Une épidémie beaucoup beaucoup plus dangereuse
Changements:
    taux de mortalité plus élévé
    infectiosité plus grande
    plus de jours pour la guérison
    prend plus de temps a etre immunisé

"""


LONG = 40
HAUT = 40
P0 = 10
P_INFECT = 60
TX_MORT = 30
NBS_J_IMM = 7
P_MASQUES = 60
P_MASQUES_MAL = 60
P_DEBUT_MASQUES = 60
P_INFECT_MASQUES = P_INFECT / 10
P_INFECT_MASQUES_MAL = P_INFECT / 2
NBS_J_INCUBATION = 2
NBS_J_GUER = 7 + NBS_J_INCUBATION
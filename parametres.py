from random import *

LONG = 40
HAUT = 40
P0 = 10
P_INFECT = 10
TX_MORT = 5
NBS_J_IMM = 4
NBS_J_INCUBATION = 4
NBS_J_GUER = 7 + NBS_J_INCUBATION  # Pour que le temps de guérison de rende pas le temps de contamination trop court
STATS = {"saine": 0, "contaminee": 0, "immunisee": 0, "decedee": 0, "mal_masquee":0, "bien_masquee":0}

# Paramètres liés aux masques
P_MASQUES = 90  # Pourcentage de la population masquée
P_MASQUES_MAL = 70  # Pourcentage de la population masquée qui met mal son masque
P_DEBUT_MASQUES = 30  # Pourcentage de la population contaminée a partir duquel les masques deviennent obligatoire
P_INFECT_MASQUES = P_INFECT / 10
P_INFECT_MASQUES_MAL = P_INFECT / 2

from choix import *

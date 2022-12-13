from random import *

"""
Cette configuration prend des valeurs aléatoires en configuration
"""

r_taille = randint(10, 100)
r_initial = randint(1, 50)
r_p_infe = randint(1, 100)
r_nbs_j_guer = randint(1, 15)
r_tx_mort = randint(1, 100)
r_nbs_j_imm = randint(1, 21)
r_nbs_j_incubation = randint(1, r_nbs_j_guer - 1)  # Le nb de jours d'incub doit etre plus petit que le nb de jours de
# guérison
r_p_masques = randint(1,100)
r_p_masques_mal = randint(1,100)
r_p_debut_masques = randint(1,100)

LONG = r_taille
HAUT = r_taille
P0 = r_initial
P_INFECT = r_p_infe
TX_MORT = r_tx_mort
NBS_J_IMM = r_nbs_j_imm
P_MASQUES = r_p_masques
P_MASQUES_MAL = r_p_masques
P_DEBUT_MASQUES = r_p_debut_masques
P_INFECT_MASQUES = P_INFECT / 10
P_INFECT_MASQUES_MAL = P_INFECT / 2
NBS_J_INCUBATION = r_nbs_j_incubation
NBS_J_GUER = r_nbs_j_guer + NBS_J_INCUBATION


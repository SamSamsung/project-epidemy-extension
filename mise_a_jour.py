from parametres import *


def voisines_contam(G, n, m, val="", nbs_j_incubation=NBS_J_INCUBATION):
    """
    Entrée:
    La grille, les positions de la cellule, une valeur vide et le nombre de jours d'incubation d'une cellule contaminée
    Sortie:
    Le nombre de cellules contaminées autour d'elles
    """
    nbs_contam = 0
    nbs_contam_masques1 = 0
    nbs_contam_masques2 = 0
    for i in range(n - 1, n + 2):
        for j in range(m - 1, m + 2):
            if i != n or j != m:  # On ne prend pas en compte la cellule principale
                if 0 <= i <= len(G) - 1 and 0 <= j <= len(G[i]) - 1:
                    if G[i][j]["valeur"] > nbs_j_incubation and G[i][j]["etat"] == "contaminee":
                        if G[i][j]["masques"] == 0:  # La cellule ne peut pas contaminée si elle est en période d'incubation
                            nbs_contam += 1  # On regarde si la cellule n'est pas masquée
                        elif G[i][j]["masques"] == 1:
                            nbs_contam_masques1 += 1
                        elif G[i][j]["masques"] == 2:
                            nbs_contam_masques2 += 1
    if val == "masques1":
        return nbs_contam_masques1
    elif val == "masques2":
        return nbs_contam_masques2
    return nbs_contam  # On retourne le nb de cellules contaminées


def transition(G, p_infect=P_INFECT, nbs_j_guer=NBS_J_GUER, tx_mort=TX_MORT, nbs_j_imm=NBS_J_IMM, p_infect_masques=P_INFECT_MASQUES, p_infect_masques_mal=P_INFECT_MASQUES_MAL):
    """
    Entrée:
    La grille, la probabilitée d'infection, le nombre de jours nécessaires à la guérison, le taux de mortalité, le nombre
    de jours nécessaires à l'immunisation, la probabilité d'infection d'une cellule masquée et la probabilité d'une
    cellule mal masquée
    Sortie:
    Une nouvelle grille ayant évolué avec les différents paramètres
    """
    G_next = [[{"etat": "saine", "valeur": 0, "masques": 0} for _ in range(len(G[i]))] for i in
              range(len(G))]  # On creer une grille
    for i in range(len(G)):
        for j in range(len(G[i])):  # On creer deux boucles pour parcourir toute la grille
            if G[i][j]["etat"] == "contaminee":  # On regarde si la cellule est contaminée
                prob = randint(1, 100)  # On tire au sort un nombre entre 1 et 100
                if prob <= tx_mort:  # On regarde si le nombre est inférieur au taux de mortalité
                    G_next[i][j]["etat"] = "decedee"
                    G_next[i][j]["masques"] = 0
                    G_next[i][j]["valeur"] = 0  # On détérmine donc la cellule comme morte
                elif G[i][j]["valeur"] == nbs_j_guer:  # On regarde si le nb de jours de la cellule est égale au nb de
                    # jours pour une guérision
                    G_next[i][j]["etat"] = "immunisee"  # On détérmine donc la cellule comme immunisée
                    G_next[i][j]["valeur"] = 0
                    G_next[i][j]["masques"] = G[i][j]["masques"]  # On garde la valeur du masque de l'ancienne grille
                else:
                    G_next[i][j]["etat"] = "contaminee"  # Sinon on détérmine la cellule comme contaminée
                    G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1  # On rajoute 1 au nb de jours
                    G_next[i][j]["masques"] = G[i][j]["masques"]  # On garde la valeur du masque de l'ancienne grille

            elif G[i][j]["etat"] == "saine":  # On regarde si la cellule est saine
                contamines = voisines_contam(G, i, j)  # On regarde combien de cellules contaminées se trouvent autour
                contamines_masques1 = voisines_contam(G, i, j, "masques1")  # On regarde cb de cellules contaminées mal masquées se trouvent autour
                contamines_masques2 = voisines_contam(G,i, j, "masques2")  # On regarde cb de cellules contaminées bien masquées se trouvent autour
                cpt, cpt_masques1, cpt_masques2 = 0, 0, 0  # On attribue 0 aux trois valeurs

                if contamines + contamines_masques1 + contamines_masques2 > 0:
                    for m in range(contamines + contamines_masques1 + contamines_masques2):  # On fait une boucle pour indice le nb de cellules contaminées autour
                        # Cela permet d'augmenter la proba d'infection en fonction du nb de cellule
                        rand, rand_masques1,rand_masques2 = randint(1,100), randint(1,100), randint(1,100)
                        if (cpt < contamines and rand <= p_infect) or (cpt_masques1 < contamines_masques1 and rand_masques1 <= p_infect_masques) \
                                or (cpt_masques2 < contamines_masques2 and rand_masques2 <= p_infect_masques_mal):
                            #  Les compteurs évitent d'avoir trop de fois la probabilité d'une cellule contaminée
                            G_next[i][j]["etat"] = "contaminee"
                            G_next[i][j]["valeur"] = 0
                            if cpt < contamines and rand <= p_infect:  # On vérifie quelle condition a été remplie
                                cpt += 1
                            elif cpt_masques1 < contamines_masques1 and rand_masques1 <= p_infect_masques:
                                cpt_masques1 += 1
                            else:
                                cpt_masques2 += 1
                            # On rajoute 1 un compteur pour éviter d'avoir trop de fois la proba d'une autre cellule
                        else:
                            G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1  # Sinon on ajoute 1 aux nombres de jours
                else:
                    G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1  # Sinon on ajoute 1 aux nombres de jours
                G_next[i][j]["masques"] = G[i][j]["masques"]

            elif G[i][j]["etat"] == "decedee":  # On regarde si la cellule est décédée
                G_next[i][j]["etat"] = "decedee"  # Son état ne change donc pas
                G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1  # Sinon on ajoute 1 aux nombres de jours
                G_next[i][j]["masques"] = 0 # On enlève le masque car la cellule est décédée

            elif G[i][j]["etat"] == "immunisee":  # On regarde si la cellule est immunisée
                if G[i][j]["valeur"] == nbs_j_imm:
                    G_next[i][j]["etat"] = "saine"  # Si son nb de jour immunisés est atteint
                    G_next[i][j]["valeur"] = 0  # elle redevient saine et on réinitialise le nombre de jours
                else:
                    G_next[i][j]["etat"] = "immunisee"  # Sinon elle reste immunisée et on rajoute 1 au nombre de jours.
                    G_next[i][j]["valeur"] = G[i][j]["valeur"] + 1  # Sinon on ajoute 1 aux nombres de jours
                G_next[i][j]["masques"] = G[i][j]["masques"]  # On garde la valeur du masque de l'ancienne grille

    return G_next  # On retourne la nouvelle grille


def statistiques(G, saine=0, contaminee=0, immunisee=0, decedee=0, mal_masque=0, bien_masque=0):
    """
    Entrée:
    La grille et les variables qui consitituent les états de toutes les cellules.
    Sortie:
    Un dictionnaire contenant toutes les statistiques de la grille
    """
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j]["masques"] != 0:
                if G[i][j]["masques"] == 1:
                    mal_masque += 1
                elif G[i][j]["masques"] == 2:
                    bien_masque += 1
            if G[i][j]["etat"] == "saine":
                saine += 1  # Si la cellule est saine, on rajoute 1 aux statistiques des cellules saines
            elif G[i][j]["etat"] == "contaminee":
                contaminee += 1  # Si la cellule est contaminée, on rajoute 1 aux statistiques des cellules contaminées
            elif G[i][j]["etat"] == "immunisee":
                immunisee += 1  # Si la cellule est immunisée, on rajoute 1 aux statistiques des cellules immunisées
            elif G[i][j]["etat"] == "decedee":
                decedee += 1  # Si la cellule est décédée, on rajoute 1 aux statistiques des cellules décédées
    return {"saine": saine, "contaminee": contaminee, "immunisee": immunisee, "decedee": decedee, "mal_masquee":mal_masque, "bien_masquee":bien_masque}


def evolution(Stats, PastStats, tour):
    """
    Entrée:
    Les statistiques de la grille, les statistiques de la grille précédente et le nombre de jours passés depuis le
    début de l'épidémie
    Sortie:
    Un dictionnaire conantenat la différence entre les statistiques de la nouvelle grille et de la grille précédente
    """
    return {"tour": tour + 1, "dif_saine": Stats["saine"] - PastStats["saine"],
            "dif_contaminee": Stats["contaminee"] - PastStats["contaminee"],
            "dif_immunisee": Stats["immunisee"] - PastStats["immunisee"],  # On soustrait le nombre des états des
            "dif_decedee": Stats["decedee"] - PastStats["decedee"],  # nouvelles cellules avec les anciennes
            "dif_mal_masquee": Stats["mal_masquee"] - PastStats["mal_masquee"],
            "diff_bien_masquee": Stats["bien_masquee"] - PastStats["bien_masquee"]}


def masques(G, p_masques=P_MASQUES, p_masques_mal=P_MASQUES_MAL):
    """
    Entrée:
    La grille, le pourcentage de personnes masqués et le pourcentages de personnes mal masquées
    Sortie:
    Une grille avec des cellules bien et mal masquées
    """
    for i in range(len(G)):
        for j in range(len(G[i])):
            rand = randint(1, 100)
            if rand <= p_masques and G[i][j]["etat"] != "decedee":  # On évite de masquer les morts
                rand2 = randint(1, 100)  # On calcule une autre proba pour savoir si la personne porte bien son masque
                if rand2 <= p_masques_mal:
                    G[i][j]["masques"] = 1  # La valeur 1 signifie que la personne porte mal son masque
                else:
                    G[i][j]["masques"] = 2  # La valeur 2 signifie que la personne porte bien son masque
    return G

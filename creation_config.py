from parametres import *


def generer(long=LONG, haut=HAUT, p0=P0):
    """
    Entrée:
    La longueur, la hauteur de la grille et le pourcentage de cellules infectées au début de la simulation
    Sortie:
    Une liste bidimensionnelle représentant une grille de simulation d'épidémie
    """
    G = [[{"etat": "saine", "valeur": 0, "masques": 0} for _ in range(long)] for i in range(haut)]  # On génère un dictionnaire vide
    for i in range(int(long * haut * p0 / 100)):  # On creer une boucle qui a pour indice la probabilité de début
        L = randint(0, long - 1)
        H = randint(0, haut - 1)
        while G[L][H]["etat"] == "contaminee":  # La boucle permet d'éviter de contaminer une cellule déja contaminée
            L = randint(0, long - 1)
            H = randint(0, haut - 1)
        G[L][H]["etat"] = "contaminee"  # On contamine les cellules selectionnées
    return G  # On retourne la grille representant la première grille



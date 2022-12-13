from parametres import *


def afficher(G, long=LONG, haut=HAUT):
    """
    Entrée:
    La longueur, la hauteur de la grille et la grille.
    Sortie:
    Un affichage visible et compréhensible de la grille
    """
    for i in range(long):
        for j in range(haut):  # On accède aux éléments de la liste grace aux deux boucles
            # On affiche un rond, coloré en fonction de leur état
            if G[i][j]["etat"] == "saine":
                if G[i][j]["valeur"] == 0:  # On vérifie s'il y a changement d'état
                    if G[i][j]["masques"] > 0:  # Si elles sont masquées, on affiche un carré soulginé
                        print("\033[4m■\033[0m", end="  ")
                    elif G[i][j]["masques"] == 0:  # Si elles ne sont pas masquées, on affiche un rond soulginé
                        print("\033[4m●\033[0m", end="  ")
                elif G[i][j]["masques"] > 0:  # Sinon on affichage un carré
                    print("■", end="  ")
                else:
                    print("●", end="  ")  # Ou alors un rond
            elif G[i][j]["etat"] == "contaminee":  # Le même processus pour les autres états
                if G[i][j]["valeur"] == 0:
                    if G[i][j]["masques"] > 0:
                        print("\033[4m\033[31m■\033[0m", end="  ")  # Le changement d'état chez la cellule se vera car
                    elif G[i][j]["masques"] == 0:  # elle sera soulignée
                        print("\033[4m\033[31m●\033[0m", end="  ")
                elif G[i][j]["masques"] > 0:
                    print("\033[1m\033[31m■\033[0m", end="  ")
                else:
                    print("\033[1m\033[31m●\033[0m", end="  ")
            elif G[i][j]["etat"] == "immunisee":
                if G[i][j]["valeur"] == 0:
                    if G[i][j]["masques"] > 0:
                        print("\033[4m\033[36m■\033[0m", end="  ")
                    elif G[i][j]["masques"] == 0:
                        print("\033[4m\033[36m●\033[0m", end="  ")
                elif G[i][j]["masques"] > 0:
                    print("\033[1m\033[36m■\033[0m", end="  ")
                else:
                    print("\033[1m\033[36m●\033[0m", end="  ")
            elif G[i][j]["etat"] == "decedee":
                if G[i][j]["valeur"] == 0 and G[i][j]["masques"] == 0:
                    print("\033[4m\033[30m●\033[0m", end="  ")
                else:                              # On ne gère pas le cas des cellules masquées car elles sont décédées
                    print("\033[1m\033[30m●\033[0m", end="  ")
        print()
    print()

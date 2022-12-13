from affichage import *
from creation_config import *
from mise_a_jour import *
from import_export import *


def boucle_finale(long=LONG, haut=HAUT, p_debut_masques=P_DEBUT_MASQUES):
    """
    Entrée:
    La longueur, la hauteur de la grille et le pourcentage de la population contaminéee pour que les masques deviennent
    obligatoire
    Sortie:
    La grille avec un nombre de tours donné et des statistiques liées aux changements
    """
    tours = int(input("Combien voulez vous faire de tours ? "))
    if input("Voulez vous récupérer la grille de la dernière partie ? Y ou N") == "Y":
        G = imp()
        if not G:
            print("Il n'y a pas de précédente sauvegarde, nous allons donc générer une grille:")
            G = generer()
    else:
        G = generer()  # Si l'utilisateur le souhaite, la grille utilisée sera celle de la dernière éxécution
    afficher(G)
    masque = True
    cpt = 0
    print("Veuillez appuyer sur n'importe quelle touche pour continuer la simulation et S pour l'arreter au prochain tour")
    while cpt < tours:  # La boucle tant que permet d'arreter la boucle si l'utilisateur a envie
        cont = input()
        if cont == "S":
            cpt = tours  # Si l'utilisateur a envie d'arreter le code, cpt sera egal a tours, ce qui fera arreter la
            # boucle
        stats1 = statistiques(G)  # On enregistre les statistiques de la grille
        G = transition(G)
        afficher(G)
        stats2 = statistiques(G)  # On enregistre les statistiques de la grille suivante
        print(stats2)  # On affiche les statistiques de la dernière grille
        print(evolution(stats2, stats1, cpt))  # On affiche la différence entre la grille précédente et la nouvelle
        if not masque:  # On implante la possibilité d'un message venant du gouvernement si une cellule ne porte pas son
            r_long = randint(1, long)  # masque. On utilise un random pour n'avoir qu'un seul message dans la console.
            r_haut = randint(1, haut)
            if G[r_long][r_haut]["masques"] == 0:
                print("Oy, la cellule a la {}e ligne et la {}e colonne, tu ne portes pas de masque. C'est HONTEUX".format(r_long+1, r_haut+1))
        cpt += 1  # On ajoute 1 au compteur pour simuler le nombre de jours
        if ((stats1["contaminee"] * 100) / (long * haut)) >= p_debut_masques and masque == True:
            #  On regarde si le pourcentage de personnes contaminées est le pourcentage requis pour le masque
            #  obligatoire et l'on creer la variable masque pour qu'elle ne soit executer qu'une fois
            G = masques(G)
            print("Les masques deviennent obligatoire : {} % de la population a été inféctée".format(int((stats1["contaminee"] * 100) / (long * haut))))
            masque = False
    exp(G)  # On exporte la grille à la fin de la boucle pour la sauvegarder pour l'éxécution suivante


boucle_finale()

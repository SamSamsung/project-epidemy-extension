from parametres import *

dem = input("Veux tu changer le mode de simulation ? Y or N")
if dem == "Y":  # On propose à l'utilisateur de changer de simulation
    print("""
    Vous avez le choix de plusieurs simulation :
        1. Le covid-19 aux Etats-Unis (même taux de mortalité mais infectiosité beauoup plus grande),
        2. Une épidémie beaucoup plus dangereuse (taux de mortalité plus élévé mais infectiosité moins grande)
        3. Une épidémie beaucoup beaucoup plus dangereuse (taux de mortalité plus élévé et infectiosité plus grande)
    """)
    choix = int(input())  # L'utilisateur doit donc chosir une des trois simulations possibles
    if choix == 1:  # On import le fichier correspondant à la configuration choisie
        from parametres1 import *
    elif choix == 2:
        from parametres2 import *
    elif choix == 3:
        from parametres3 import *
    else:
        print(
            "Vous ne savez pas choisir nous allons donc choisir pour vous :")  # Dans le cas ou l'utilisateur ne
        # saisit pas un bon chiffre
        from parametres4 import *

        print("c'est donc la configuration avec des paramètres aléatoires qui est choisie")

print("""
Vos parametres sont donc :
    - Superficie : {} x {}
    - Nombre d'infectés au premier tour : {} %
    - Probabilité d'infectiosité : {} %
    - Le nombre de jour necessaires à la guérison : {}
    - Le taux de mortalité : {} %
    - Le nombre de jour durant lesquels une cellule est immunisée : {}
    - Le nombre de jour durant lesquels la cellule contaminée sera en incubation : {}
    - Le pourcentage de cellule portant des masques : {}
    - Le pourcentage de cellule portant mal les masques : {}
    - Le pourcentage de cellules contaminées nécessaires à la décision du port du masque obligatoire {}
    - La probabilité d'infection d'une cellule contaminée masquée : {}
    - La probabilité d'infection d'une cellule contaminée mal masquée : {}
""".format(LONG, HAUT, P0, P_INFECT, NBS_J_GUER, TX_MORT, NBS_J_GUER, NBS_J_INCUBATION, P_MASQUES, P_MASQUES_MAL, P_DEBUT_MASQUES, P_INFECT_MASQUES, P_INFECT_MASQUES_MAL))  # On affichage touts les parametres

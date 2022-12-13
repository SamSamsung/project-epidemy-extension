def exp(G, nom_fichier="sauvegarde", separateur="; "):
    """
    Entrée : une liste de listes et une chaîne de caractères correspondante au nom d'un fichier
    Sortie : écriture des élements de la liste de liste L dans le fichier, ligne par ligne et élément par élément (séparés par un espace par défaut)
    """
    F = open(nom_fichier, "w")  # on ouvre le fichier en mode "w" ("w" = mode écriture qui écrase le contenu déjà
    # existant ; "r" = mode lecture seule ; "a" : mode append, qui rajoute le texte à la fin du fichier)
    for i in range(len(G)):
        for j in range(len(G[i])):
            F.write(str(G[i][j]))  # on écrit le j-ème mot de la i-ème ligne de L
            if j < len(G[i]) - 1:  # ajout du séparateur s'il ne s'agit pas du dernier élément de la ligne
                F.write(separateur)
        F.write("\n")  # pour rajouter des sauts de ligne (s'ils ne sont pas déjà gérés dans le fichier)
    F.close()  # il faut impérativement fermer le fichier pour qu'il soit bien sauvegardé


def imp(nom_fichier = "sauvegarde", separateur=";"):
    """
    Entrée : une chaîne de caractères correspondante au nom d'un fichier
    Sortie : la liste des lignes du fichier, chaque ligne étant donnée sous forme de la liste de ses mots (séparés par un espace par défaut)
    """
    L = []
    try:
        with open(nom_fichier, "r") as f:  # permet d'ouvrir un fichier et de le fermer automatiquement
            for ligne in f:  # on parcourt l'ensemble du fichier (effectué ligne par ligne)
                L.append(ligne.split(separateur))  # ligne.split() est une liste dont les éléments sont les mots de
                # ligne, séparés par le caractère separateur

    except FileNotFoundError:  # au cas où le fichier n'existe pas (et dans ce cas, la liste reste vide
        # et revient à créer un fichier vide)
        pass
    for i in range(len(L)):
        for j in range(len(L[i])):
            L[i][j] = eval(L[i][j])  # On retransforme L[i][j] en dictionnaire pour éviter que la fonction
            # "transition" cherche un indice de liste en chaine de caractère
    G = []
    for w in range(len(L)):
        G.append([])
        for g in range(len(L[w])):
            G[w].append(L[w][g])  # On utilise G pour la grille finale
    return G

def tri(listeATrier):
    length = 0
    for n in listeATrier:
        length += 1
    coupTotal = 0
    for nb in range(length):
        for i in range(length - nb):
            if i+1 >= length - nb:
                break
            elif int(listeATrier[i]) > int(listeATrier[i+1]):
                valeurPremierCaractere = listeATrier[i]
                listeATrier[i] = listeATrier[i+1]
                listeATrier[i+1] = valeurPremierCaractere
                coupTotal += 1
    print(f"Nombre total de coups nécessaires pour trier la liste : {coupTotal}")
    print(f"Liste triée : {listeATrier}")

listeATrier = [input("Rentrez le 1er nombre de la liste : "),
               input("Rentrez le 2e nombre de la liste : "),
               input("Rentrez le 3e nombre de la liste : "),
               input("Rentrez le 4e nombre de la liste : "),
               input("Rentrez le 5e nombre de la liste : "),
               input("Rentrez le 6e nombre de la liste : "),
               input("Rentrez le 7e nombre de la liste : "),
               input("Rentrez le 8e nombre de la liste : "),
               input("Rentrez le 9e nombre de la liste : "),
               input("Rentrez le 10e nombre de la liste : ")]

tri(listeATrier)
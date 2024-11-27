def my_long_word(nombre, chaine):
    chaineRetourne = ""
    chaineTemporaire = ""
    nbCaractere = 0

    longueurChaine = 0
    for y in chaine:
        longueurChaine += 1

    for i in range(longueurChaine):
        if chaine[i] == " " or chaine[i] == ",":
            for n in chaineTemporaire:
                nbCaractere += 1
            if nbCaractere > nombre:
                chaineRetourne += chaineTemporaire
            chaineTemporaire = ""
            nbCaractere = 0
        elif i == longueurChaine-1:
            for n in chaineTemporaire:
                nbCaractere += 1
            if nbCaractere > nombre:
                    chaineRetourne += chaineTemporaire
                    chaineRetourne += chaine[i]
            chaineTemporaire = ""
            nbCaractere = 0
        chaineTemporaire += chaine[i]

    print(chaineRetourne)


my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
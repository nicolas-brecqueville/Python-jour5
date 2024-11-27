def list():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    sommeNombrePair = 0
    for i in L:
        if i % 2 == 0:
            sommeNombrePair += i
    print(f"La somme du tableau pair est de : {sommeNombrePair}.")

list()
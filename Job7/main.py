def list():
    L = [8, 24,48,2,16]
    nombreMultiple3 = 0
    for i in L:
        if i % 3 == 0:
            nombreMultiple3 += 1
    print(f"Il y a {nombreMultiple3} nombres multiple de 3 dans cette chaine.")

list()
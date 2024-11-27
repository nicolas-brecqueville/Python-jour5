def list():
    L = [1, 2, 3, 4, 5]
    print(L)
    premiereValeur = L[0]
    L[0] = L[-1]
    L[-1] = premiereValeur
    print(L)

list()
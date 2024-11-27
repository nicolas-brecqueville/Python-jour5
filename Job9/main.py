def list():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    # maximum = L[0]
    # minimum = L[0]
    # for i in range(len(L)):
    #     if i+1 >= len(L):
    #         break
    #     elif maximum < L[i+1]:
    #         maximum = L[i+1]
    #     elif minimum > L[i+1]:
    #         minimum = L[i+1]
    # print(f"La valeur maximum du tableau est : {maximum}")
    # print(f"La valeur minimum du tableau est : {minimum}")

    print(f"La valeur minimum du tableau est : {max(L)}")
    print(f"La valeur minimum du tableau est : {min(L)}")

list()
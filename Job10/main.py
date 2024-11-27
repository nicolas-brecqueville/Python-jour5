def list():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    quotient = 1
    for i in L:
        if 25 <= i <= 90:
            quotient *= i
    print(f"Le quotient des nombres de la liste compris dans l'intervalle [25, 90] est : {quotient}")

list()
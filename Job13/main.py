def list():
    L = [10, 20, 30, 20, 10, 10, 50, 60, 40, 80, 50, 40]
    length = 0

    for n in L:
        length += 1

    i = 0

    while i < length:
        n = i + 1
        while n < length:
            if L[i] == L[n]:
                del L[n]
                length -= 1
            else:
                n += 1
        i += 1
    print(L)

list()

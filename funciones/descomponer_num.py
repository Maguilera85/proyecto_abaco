
def descomponer(numero):
    largo = len(numero)
    if largo == 1:
        u = numero[0]
        u = int(u)
        return u
    elif largo == 2:
        d = numero[0]
        d = int(d)
        u = numero[1]
        u = int(u)
        return d, u
    elif largo == 3:
        c = numero[0]
        c = int(c)
        d = numero[1]
        d = int(d)
        u = numero[2]
        u = int(u)
        return c, d, u
    elif largo == 4:
        um = numero[0]
        um = int(um)
        c = numero[1]
        c = int(c)
        d = numero[2]
        d = int(d)
        u = numero[3]
        u = int(u)
        return um, c, d, u
    elif largo == 5:
        dm = numero[0]
        dm = int(dm)
        um = numero[1]
        um = int(um)
        c = numero[2]
        c = int(c)
        d = numero[3]
        d = int(d)
        u = numero[4]
        u = int(u)
        return dm, um, c, d, u
    elif largo == 6:
        cm = numero[0]
        cm = int(cm)
        dm = numero[1]
        dm = int(dm)
        um = numero[2]
        um = int(um)
        c = numero[3]
        c = int(c)
        d = numero[4]
        d = int(d)
        u = numero[5]
        u = int(u)
        return cm, dm, um, c, d, u


if __name__ == "__main__":
    test = descomponer('123456')
    print(test)
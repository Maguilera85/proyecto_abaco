def imprimir_abaco(cm, dm, um, c, d, u):
    # Estas son las coordenadas del abaco
    tablero = { 54: '   ' , 45: '   ' , 36: '   ' , 27: '   ' , ("d", 9): '   ' , ("u", 9): '   ' ,
                53: '   ' , 44: '   ' , 35: '   ' , 26: '   ' , ("d", 8): '   ' , ("u", 8): '   ' ,
                52: '   ' , 43: '   ' , 34: '   ' , 25: '   ' , ("d", 7): '   ' , ("u", 7): '   ' , 
                51: '   ' , 42: '   ' , 33: '   ' , 24: '   ' , ("d", 6): '   ' , ("u", 6): '   ' ,
                50: '   ' , 41: '   ' , 32: '   ' , 23: '   ' , ("d", 5): '   ' , ("u", 5): '   ' ,
                49: '   ' , 40: '   ' , 31: '   ' , 22: '   ' , ("d", 4): '   ' , ("u", 4): '   ' ,
                48: '   ' , 39: '   ' , 30: '   ' , 21: '   ' , ("d", 3): '   ' , ("u", 3): '   ' ,
                47: '   ' , 38: '   ' , 29: '   ' , 20: '   ' , ("d", 2): '   ' , ("u", 2): '   ' ,
                46: '   ' , 37: '   ' , 28: '   ' , 19: '   ' , ("d", 1): '   ' , ("u", 1): '   ' }

    posiciones = [("cm", cm), ("dm", dm), ("um", um), ("c", c), ("d", d), ("u", u)]
    for elemento in posiciones:
        for idx in range(1, elemento[1] + 1):
            tablero[(elemento[0], idx)] = "XXX"

    # imprime abaco visual
    print()
    print("  +---+       +---+       +---+       +---+       +---+       +---+")
    print("  |" + tablero[54] + "|       |" + tablero[45] + "|       |" + tablero[36] + "|       |" + tablero[27] + "|       |" + tablero[("d", 9)] + "|       |" + tablero[("u", 9)] + "|")
    print("  |" + tablero[53] + "|       |" + tablero[44] + "|       |" + tablero[35] + "|       |" + tablero[26] + "|       |" + tablero[("d", 8)] + "|       |" + tablero[("u", 8)] + "|")
    print("  |" + tablero[52] + "|       |" + tablero[43] + "|       |" + tablero[34] + "|       |" + tablero[25] + "|       |" + tablero[("d", 7)] + "|       |" + tablero[("u", 7)] + "|")
    print("  |" + tablero[51] + "|       |" + tablero[42] + "|       |" + tablero[33] + "|       |" + tablero[24] + "|       |" + tablero[("d", 6)] + "|       |" + tablero[("u", 6)] + "|")
    print("  |" + tablero[50] + "|       |" + tablero[41] + "|       |" + tablero[32] + "|       |" + tablero[23] + "|       |" + tablero[("d", 5)] + "|       |" + tablero[("u", 5)] + "|")
    print("  |" + tablero[49] + "|       |" + tablero[40] + "|       |" + tablero[31] + "|       |" + tablero[22] + "|       |" + tablero[("d", 4)] + "|       |" + tablero[("u", 4)] + "|")
    print("  |" + tablero[48] + "|       |" + tablero[39] + "|       |" + tablero[30] + "|       |" + tablero[21] + "|       |" + tablero[("d", 3)] + "|       |" + tablero[("u", 3)] + "|")
    print("  |" + tablero[47] + "|       |" + tablero[38] + "|       |" + tablero[29] + "|       |" + tablero[20] + "|       |" + tablero[("d", 2)] + "|       |" + tablero[("u", 2)] + "|")
    print("  |" + tablero[46] + "|       |" + tablero[37] + "|       |" + tablero[28] + "|       |" + tablero[19] + "|       |" + tablero[("d", 1)] + "|       |" + tablero[("u", 1)] + "|")
    print("__+---+_______+---+_______+---+_______+---+_______+---+_______+---+__")
    print("|___________________________________________________________________|")
    print()

imprimir_abaco(1, 1, 1, 1, 1, 1)


# descompone el numero ingresado por el usuario
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

# def funcion_punto():


# imprime registros de datos ingresados por usuario
def imprimir_reg(lista):
    for elementos in lista:
        print(elementos)
# inicia el programa
def abaco_inicio():
    registro = []
    print("Bienvenido al ABACO")
    print("ingrese un numeroero para graficar en el ABACO o escriba 'salir' para terminar el programa")
    while True:
        dato = input(">> ")
        if dato != 'salir':
            dicc = dict(enumerate(dato))
            registro.append(dato)
            print(dicc)
            descomponer(dato)
            print(dato)
        else:
            print("\nEste fue el registro de tus solicitudes")
            imprimir_reg(registro)
            print("¡Hasta pronto!")
            break


if __name__ == "__main__":
    abaco_inicio()
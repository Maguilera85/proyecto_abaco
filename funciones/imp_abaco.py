def imprimir_abaco(cm, dm, um, c, d, u):
    # Estas son las coordenadas del abaco
    tablero = { ("cm", 9): '   ' , ("dm", 9): '   ' , ("um", 9): '   ' , ("c", 9): '   ' , ("d", 9): '   ' , ("u", 9): '   ' ,
                ("cm", 8): '   ' , ("dm", 8): '   ' , ("um", 8): '   ' , ("c", 8): '   ' , ("d", 8): '   ' , ("u", 8): '   ' ,
                ("cm", 7): '   ' , ("dm", 7): '   ' , ("um", 7): '   ' , ("c", 7): '   ' , ("d", 7): '   ' , ("u", 7): '   ' , 
                ("cm", 6): '   ' , ("dm", 6): '   ' , ("um", 6): '   ' , ("c", 6): '   ' , ("d", 6): '   ' , ("u", 6): '   ' ,
                ("cm", 5): '   ' , ("dm", 5): '   ' , ("um", 5): '   ' , ("c", 5): '   ' , ("d", 5): '   ' , ("u", 5): '   ' ,
                ("cm", 4): '   ' , ("dm", 4): '   ' , ("um", 4): '   ' , ("c", 4): '   ' , ("d", 4): '   ' , ("u", 4): '   ' ,
                ("cm", 3): '   ' , ("dm", 3): '   ' , ("um", 3): '   ' , ("c", 3): '   ' , ("d", 3): '   ' , ("u", 3): '   ' ,
                ("cm", 2): '   ' , ("dm", 2): '   ' , ("um", 2): '   ' , ("c", 2): '   ' , ("d", 2): '   ' , ("u", 2): '   ' ,
                ("cm", 1): '   ' , ("dm", 1): '   ' , ("um", 1): '   ' , ("c", 1): '   ' , ("d", 1): '   ' , ("u", 1): '   ' }

    posiciones = [("cm", cm), ("dm", dm), ("um", um), ("c", c), ("d", d), ("u", u)]
    for elemento in posiciones:
        for idx in range(1, elemento[1] + 1):
            tablero[(elemento[0], idx)] = "XXX"

    # imprime abaco visual
    print()
    print("  +---+       +---+       +---+       +---+       +---+       +---+")
    print("  |" + tablero[("cm", 9)] + "|       |" + tablero[("dm", 9)] + "|       |" + tablero[("um", 9)] + "|       |" + tablero[("c", 9)] + "|       |" + tablero[("d", 9)] + "|       |" + tablero[("u", 9)] + "|")
    print("  |" + tablero[("cm", 8)] + "|       |" + tablero[("dm", 8)] + "|       |" + tablero[("um", 8)] + "|       |" + tablero[("c", 8)] + "|       |" + tablero[("d", 8)] + "|       |" + tablero[("u", 8)] + "|")
    print("  |" + tablero[("cm", 7)] + "|       |" + tablero[("dm", 7)] + "|       |" + tablero[("um", 7)] + "|       |" + tablero[("c", 7)] + "|       |" + tablero[("d", 7)] + "|       |" + tablero[("u", 7)] + "|")
    print("  |" + tablero[("cm", 6)] + "|       |" + tablero[("dm", 6)] + "|       |" + tablero[("um", 6)] + "|       |" + tablero[("c", 6)] + "|       |" + tablero[("d", 6)] + "|       |" + tablero[("u", 6)] + "|")
    print("  |" + tablero[("cm", 5)] + "|       |" + tablero[("dm", 5)] + "|       |" + tablero[("um", 5)] + "|       |" + tablero[("c", 5)] + "|       |" + tablero[("d", 5)] + "|       |" + tablero[("u", 5)] + "|")
    print("  |" + tablero[("cm", 4)] + "|       |" + tablero[("dm", 4)] + "|       |" + tablero[("um", 4)] + "|       |" + tablero[("c", 4)] + "|       |" + tablero[("d", 4)] + "|       |" + tablero[("u", 4)] + "|")
    print("  |" + tablero[("cm", 3)] + "|       |" + tablero[("dm", 3)] + "|       |" + tablero[("um", 3)] + "|       |" + tablero[("c", 3)] + "|       |" + tablero[("d", 3)] + "|       |" + tablero[("u", 3)] + "|")
    print("  |" + tablero[("cm", 2)] + "|       |" + tablero[("dm", 2)] + "|       |" + tablero[("um", 2)] + "|       |" + tablero[("c", 2)] + "|       |" + tablero[("d", 2)] + "|       |" + tablero[("u", 2)] + "|")
    print("  |" + tablero[("cm", 1)] + "|       |" + tablero[("dm", 1)] + "|       |" + tablero[("um", 1)] + "|       |" + tablero[("c", 1)] + "|       |" + tablero[("d", 1)] + "|       |" + tablero[("u", 1)] + "|")
    print("__+---+_______+---+_______+---+_______+---+_______+---+_______+---+__")
    print("|___________________________________________________________________|")
    print()

    if __name__ == "__main__":
        imprimir_abaco(1, 2, 3, 4, 5, 6)
        
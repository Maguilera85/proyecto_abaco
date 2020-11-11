# Estas son las coordenadas del abaco
def coodenadas():
    tablero = {54: '   ' , 45: '   ' , 36: '   ' , 27: '   ' , 18: '   ' , 9: '   ' ,
            53: '   ' , 44: '   ' , 35: '   ' , 26: '   ' , 17: '   ' , 8: '   ' ,
            52: '   ' , 43: '   ' , 34: '   ' , 25: '   ' , 16: '   ' , 7: '   ' , 
            51: '   ' , 42: '   ' , 33: '   ' , 24: '   ' , 15: '   ' , 6: '   ' ,
            50: '   ' , 41: '   ' , 32: '   ' , 23: '   ' , 14: '   ' , 5: '   ' ,
            49: '   ' , 40: '   ' , 31: '   ' , 22: '   ' , 13: '   ' , 4: '   ' ,
            48: '   ' , 39: '   ' , 30: '   ' , 21: '   ' , 12: '   ' , 3: '   ' ,
            47: '   ' , 38: '   ' , 29: '   ' , 20: '   ' , 11: '   ' , 2: '   ' ,
            46: '   ' , 37: '   ' , 28: '   ' , 19: '   ' , 10: '   ' , 1: '   ' }
           
# imprime abaco visual
def tablero_visual():
    print()
    print("  +---+       +---+       +---+       +---+       +---+       +---+")
    print("  |" + tablero[54] + "|       |" + tablero[45] + "|       |" + tablero[36] + "|       |" + tablero[27] + "|       |" + tablero[18] + "|       |" + tablero[9] + "|")
    print("  |" + tablero[53] + "|       |" + tablero[44] + "|       |" + tablero[35] + "|       |" + tablero[26] + "|       |" + tablero[17] + "|       |" + tablero[8] + "|")
    print("  |" + tablero[52] + "|       |" + tablero[43] + "|       |" + tablero[34] + "|       |" + tablero[25] + "|       |" + tablero[16] + "|       |" + tablero[7] + "|")
    print("  |" + tablero[51] + "|       |" + tablero[42] + "|       |" + tablero[33] + "|       |" + tablero[24] + "|       |" + tablero[15] + "|       |" + tablero[6] + "|")
    print("  |" + tablero[50] + "|       |" + tablero[41] + "|       |" + tablero[32] + "|       |" + tablero[23] + "|       |" + tablero[14] + "|       |" + tablero[5] + "|")
    print("  |" + tablero[49] + "|       |" + tablero[40] + "|       |" + tablero[31] + "|       |" + tablero[22] + "|       |" + tablero[13] + "|       |" + tablero[4] + "|")
    print("  |" + tablero[48] + "|       |" + tablero[39] + "|       |" + tablero[30] + "|       |" + tablero[21] + "|       |" + tablero[12] + "|       |" + tablero[3] + "|")
    print("  |" + tablero[47] + "|       |" + tablero[38] + "|       |" + tablero[29] + "|       |" + tablero[20] + "|       |" + tablero[11] + "|       |" + tablero[2] + "|")
    print("  |" + tablero[46] + "|       |" + tablero[37] + "|       |" + tablero[28] + "|       |" + tablero[19] + "|       |" + tablero[10] + "|       |" + tablero[1] + "|")
    print("__+---+_______+---+_______+---+_______+---+_______+---+_______+---+__")
    print("|___________________________________________________________________|")
    print()


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
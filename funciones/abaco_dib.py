theBoard = {54: '   ' , 45: '   ' , 36: '   ' , 27: '   ' , 18: '   ' , 9: '   ' ,
            53: '   ' , 44: '   ' , 35: '   ' , 26: '   ' , 17: '   ' , 8: '   ' ,
            52: '   ' , 43: '   ' , 34: '   ' , 25: '   ' , 16: '   ' , 7: '   ' , 
            51: '   ' , 42: '   ' , 33: '   ' , 24: '   ' , 15: '   ' , 6: '   ' ,
            50: '   ' , 41: '   ' , 32: '   ' , 23: '   ' , 14: '   ' , 5: '   ' ,
            49: '   ' , 40: '   ' , 31: '   ' , 22: '   ' , 13: '   ' , 4: '   ' ,
            48: '   ' , 39: '   ' , 30: '   ' , 21: '   ' , 12: '   ' , 3: '   ' ,
            47: '   ' , 38: '   ' , 29: '   ' , 20: '   ' , 11: '   ' , 2: '   ' ,
            46: '   ' , 37: '   ' , 28: '   ' , 19: '   ' , 10: '   ' , 1: '   ' }
           

board_keys = []

for key in theBoard:
    board_keys.append(key)

print()
print("  +---+       +---+       +---+       +---+       +---+       +---+")
print("  |" + theBoard[54] + "|       |" + theBoard[45] + "|       |" + theBoard[36] + "|       |" + theBoard[27] + "|       |" + theBoard[18] + "|       |" + theBoard[9] + "|")
print("  |" + theBoard[53] + "|       |" + theBoard[44] + "|       |" + theBoard[35] + "|       |" + theBoard[26] + "|       |" + theBoard[17] + "|       |" + theBoard[8] + "|")
print("  |" + theBoard[52] + "|       |" + theBoard[43] + "|       |" + theBoard[34] + "|       |" + theBoard[25] + "|       |" + theBoard[16] + "|       |" + theBoard[7] + "|")
print("  |" + theBoard[51] + "|       |" + theBoard[42] + "|       |" + theBoard[33] + "|       |" + theBoard[24] + "|       |" + theBoard[15] + "|       |" + theBoard[6] + "|")
print("  |" + theBoard[50] + "|       |" + theBoard[41] + "|       |" + theBoard[32] + "|       |" + theBoard[23] + "|       |" + theBoard[14] + "|       |" + theBoard[5] + "|")
print("  |" + theBoard[49] + "|       |" + theBoard[40] + "|       |" + theBoard[31] + "|       |" + theBoard[22] + "|       |" + theBoard[13] + "|       |" + theBoard[4] + "|")
print("  |" + theBoard[48] + "|       |" + theBoard[39] + "|       |" + theBoard[30] + "|       |" + theBoard[21] + "|       |" + theBoard[12] + "|       |" + theBoard[3] + "|")
print("  |" + theBoard[47] + "|       |" + theBoard[38] + "|       |" + theBoard[29] + "|       |" + theBoard[20] + "|       |" + theBoard[11] + "|       |" + theBoard[2] + "|")
print("  |" + theBoard[46] + "|       |" + theBoard[37] + "|       |" + theBoard[28] + "|       |" + theBoard[19] + "|       |" + theBoard[10] + "|       |" + theBoard[1] + "|")
print("__+---+_______+---+_______+---+_______+---+_______+---+_______+---+__")
print("|___________________________________________________________________|")
print()



# lista = []
# print("Bienvenidos al ABACO, para salir escriba: S, s, salir")
# while True:
#     # se gurdan digitos en diccionario
#     numero = input('ingrese numero: ')
#     dicc = dict(enumerate(numero))
#     #se guarda numeros en lista
#     lista.append(numero)    
#     # estes es la salida del codigo
#     if numero == 'S' or numero == 's' or numero == 'salir':     
#         break
#     else:
#         continue

# numeros = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6'}
numeros = {0 : '1'}
unidad = 0
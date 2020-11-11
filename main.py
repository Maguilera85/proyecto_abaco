lista = []
print("Bienvenidos al ABACO, para salir escriba: S, s, salir")
while True:
    # se gurdan digitos en diccionario
    numeroero = input('ingrese numeroero: ')
    dicc = dict(enumeroerate(numeroero))
    # aqui se ejecuta la funcion graficar
    print(dicc)
    # largo = len(dicc)
    # print(largo)
     
    #se guarda numeroeros en lista
    lista.append(numeroero)
    
    # estes es la salida del codigo
    if numeroero == 'S' or numeroero == 's' or numeroero == 'salir':
      
        break
    else:
        continue




# print(lista)
for i in range(len(lista) -1):

    print("{:,}".format(i).replace(',','~').replace('.',',').replace('~','.'))  



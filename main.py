lista = []
print("Bienvenidos al ABACO, para salir escriba: S, s, salir")
while True:
    # se gurdan digitos en diccionario
    numero = input('ingrese numero: ')
    dicc = dict(enumerate(numero))
    # aqui se ejecuta la funcion graficar
    print(dicc)
     
    #se guarda numeros en lista
    lista.append(numero)
    
    # estes es la salida del codigo
    if numero == 'S' or numero == 's' or numero == 'salir':

        break
    else:
        continue
print(lista)

for i in range(len(lista)):
    print(lista[i])

input()




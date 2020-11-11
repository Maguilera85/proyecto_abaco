import funciones as fun

registro = []
fun.logo()
print("\nBienvenido al ABACO")
print("ingrese un número para graficar en el ABACO o escriba 'salir' para terminar el programa")
while True:
    dato = input(">> ")
    if dato != 'salir':
        dicc = dict(enumerate(dato))
        #registro.append(dato)
        print(dicc)
        cm,dm,um,c,d,u =  fun.descomponer(dato)
        #print(dato)
        fun.imprimir_abaco(cm,dm,um,c,d,u)
        lo_quesea = fun.funcion_punto(dato)
        registro.append(lo_quesea)
        #print(registro)

    else:
        print("\nEste fue el registro de tus solicitudes")
        fun.imprimir_reg(registro)
        print("¡Hasta pronto!")
        break

input()
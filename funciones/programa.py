


def programa():
    dicc_numeros = {}
    
    print("Bienvenidos al ABACO \n para terminar el programa escribe 'salir'")
    
    while True:
        entrada = input("Ingrese un numero: ")
        if entrada == 'salir' or entrada == 'Salir':
            print("Estas fueron tus busquedas ¡Hasta pronto!")
            print(dicc_numeros)
            break
        else:
            dicc_numeros['intento'] = entrada
            print(dicc_numeros)



if __name__ == "__main__":
    programa()
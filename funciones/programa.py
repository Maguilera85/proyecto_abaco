


def programa():
    dicc_numeroeros = {}
    
    print("Bienvenidos al ABACO \n para terminar el programa escribe 'salir'")
    
    while True:
        entrada = input("Ingrese un numeroero: ")
        if entrada == 'salir' or entrada == 'Salir':
            print("Estas fueron tus busquedas ¡Hasta pronto!")
            print(dicc_numeroeros)
            break
        else:
            dicc_numeroeros['intento'] = entrada
            print(dicc_numeroeros)



if __name__ == "__main__":
    programa()
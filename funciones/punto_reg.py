# agrega punto mil
def funcion_punto(registro):
    registro2 = str(registro)
    lo_quesea2 = registro2[:-3]+ "." + registro2[-3:]
    return lo_quesea2


# imprime registros de datos ingresados por usuario
def imprimir_reg(lista):
    for elementos in lista:
        print(elementos)


if __name__ == "__main__":
    print(funcion_punto('123456'))
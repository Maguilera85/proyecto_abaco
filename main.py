lista = []

while True:
	# se gurdan digitos en diccionario
	numero = input('ingrese numero: ')
	dicc = dict(enumerate(numero))
	# aqui se ejecuta la funcion graficar
	print(dicc)
     
    #se guarda numeros en lista
	lista.append(numero)
	r = input('Desea salir: si o no:')

	if r == 'no':
		continue
	else:
		break

print(lista)

for i in range(len(lista)):
	print(lista[i])

input()




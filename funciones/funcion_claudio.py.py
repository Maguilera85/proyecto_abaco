
# No me ha duncionado como concaquenar horizontalmente estos strigs
ABACO = ['''             +-+
             | |
             | |
             | |
             | |
             | |
             | |
             | |
             | |
             | |
             +-+

            ''']

print(str(ABACO[0]) + str(ABACO[0]))
n = type(ABACO[0])
print(n)


# Solo imprimir verticalmente
def funcion_barra(n):

      if n == 0:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('+-+')
      elif n == 1:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('XXX')
            print('+-+')
      elif n == 2:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 3:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 4:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 5:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('| |')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 6:
            print('+-+')
            print('| |')
            print('| |')
            print('| |')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 7:
            print('+-+')
            print('| |')
            print('| |')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 8:
            print('+-+')
            print('| |')
            print('xxx')
            print('xxx')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      elif n == 9:
            print('+-+')
            print('xxx')
            print('xxx')
            print('xxx')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('XXX')
            print('+-+')
      else:
            print('ingrese correctamente')
      

while True:
      n = int(input('ingrese un numeroero: '))
      funcion_barra(n)










# no me resulta reasignar el valor al tablero
def graficar(argumentos):

      print()
      print("  +---+       +---+       +---+       +---+       +---+       +---+")
      print("  |" + tablero['cm9'] + "|       |" + tablero['dm9'] + "|       |" + tablero['um9'] + "|       |" + tablero['c9'] + "|       |" + tablero['d9'] + "|       |" + tablero['u9'] + "|")
      print("  |" + tablero['cm8'] + "|       |" + tablero['dm8'] + "|       |" + tablero['um8'] + "|       |" + tablero['c8'] + "|       |" + tablero['d8'] + "|       |" + tablero['u8'] + "|")
      print("  |" + tablero['cm7'] + "|       |" + tablero['dm7'] + "|       |" + tablero['um7'] + "|       |" + tablero['c7'] + "|       |" + tablero['d7'] + "|       |" + tablero['u7'] + "|")
      print("  |" + tablero['cm6'] + "|       |" + tablero['dm6'] + "|       |" + tablero['um6'] + "|       |" + tablero['c6'] + "|       |" + tablero['d6'] + "|       |" + tablero['u6'] + "|")
      print("  |" + tablero['cm5'] + "|       |" + tablero['dm5'] + "|       |" + tablero['um5'] + "|       |" + tablero['c5'] + "|       |" + tablero['d5'] + "|       |" + tablero['u5'] + "|")
      print("  |" + tablero['cm4'] + "|       |" + tablero['dm4'] + "|       |" + tablero['um4'] + "|       |" + tablero['c4'] + "|       |" + tablero['d4'] + "|       |" + tablero['u4'] + "|")
      print("  |" + tablero['cm3'] + "|       |" + tablero['dm3'] + "|       |" + tablero['um3'] + "|       |" + tablero['c3'] + "|       |" + tablero['d3'] + "|       |" + tablero['u3'] + "|")
      print("  |" + tablero['cm2'] + "|       |" + tablero['dm2'] + "|       |" + tablero['um2'] + "|       |" + tablero['c2'] + "|       |" + tablero['d2'] + "|       |" + tablero['u2'] + "|")
      print("  |" + tablero['cm1'] + "|       |" + tablero['dm1'] + "|       |" + tablero['um1'] + "|       |" + tablero['c1'] + "|       |" + tablero['d1'] + "|       |" + tablero['u1'] + "|")
      print("__+---+_______+---+_______+---+_______+---+_______+---+_______+---+__")
      print("|___________________________________________________________________|")
      print()


tablero = {'cm9': '   ', 'dm9': '   ', 'um9': '   ', 'c9': '   ', 'd9': '   ', 'u9': '   ',
            'cm8': '   ', 'dm8': '   ', 'um8': '   ', 'c8': '   ', 'd8': '   ', 'u8': '   ',
            'cm7': '   ', 'dm7': '   ', 'um7': '   ', 'c7': '   ', 'd7': '   ', 'u7': '   ', 
            'cm6': '   ', 'dm6': '   ', 'um6': '   ', 'c6': '   ', 'd6': '   ', 'u6': '   ',
            'cm5': '   ', 'dm5': '   ', 'um5': '   ', 'c5': '   ', 'd5': '   ', 'u5': '   ',
            'cm4': '   ', 'dm4': '   ', 'um4': '   ', 'c4': '   ', 'd4': '   ', 'u4': '   ',
            'cm3': '   ', 'dm3': '   ', 'um3': '   ', 'c3': '   ', 'd3': '   ', 'u3': '   ',
            'cm2': '   ', 'dm2': '   ', 'um2': '   ', 'c2': '   ', 'd2': '   ', 'u2': '   ',
            'cm1': '   ', 'dm1': '   ', 'um1': '   ', 'c1': '   ', 'd1': '   ', 'u1': '   '}

tablero['cm9'] = 'x'
if tablero['cm9'] == 'x':
      graficar()



input()
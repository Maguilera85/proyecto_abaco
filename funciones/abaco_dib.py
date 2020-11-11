theBoard = {'cm9': ' ' , 'dm9': ' ' , 'um9': ' ' , 'c9': ' ' , 'd9': ' ' , 'u9': ' ' ,
            'cm8': ' ' , 'dm8': ' ' , 'um8': ' ' , 'c8': ' ' , 'd8': ' ' , 'u8': ' ' ,
            'cm7': ' ' , 'dm7': ' ' , 'um7': ' ' , 'c7': ' ' , 'd7': ' ' , 'u7': ' ' , 
            'cm6': ' ' , 'dm6': ' ' , 'um6': ' ' , 'c6': ' ' , 'd6': ' ' , 'u6': ' ' ,
            'cm5': ' ' , 'dm5': ' ' , 'um5': ' ' , 'c5': ' ' , 'd5': ' ' , 'u5': ' ' ,
            'cm4': ' ' , 'dm4': ' ' , 'um4': ' ' , 'c4': ' ' , 'd4': ' ' , 'u4': ' ' ,
            'cm3': ' ' , 'dm3': ' ' , 'um3': ' ' , 'c3': ' ' , 'd3': ' ' , 'u3': ' ' ,
            'cm2': ' ' , 'dm2': ' ' , 'um2': ' ' , 'c2': ' ' , 'd2': ' ' , 'u2': ' ' ,
            'cm1': ' ' , 'dm1': ' ' , 'um1': ' ' , 'c1': ' ' , 'd1': ' ' , 'u1': ' ' ,}

board_keys = []

for key in theBoard:
    board_keys.append(key)

"""– 1 unidad = 1 unidad
   – 1 decena = 10 unidades
   – 1 centena = 100 unidades
   – 1 unidad de mil = 1 000 unidades
   – 1 decena de mil = 10 000 unidades
   – 1 centena de mil = 100 000 unidades """

print()
print("  +---+       +---+       +---+       +---+       +---+       +---+")
print("  |" + theBoard['cm9'] + "|       |" + theBoard['dm9'] + "|       |" + theBoard['um9'] + "|       |" + theBoard['c9'] + "|       |" + theBoard['d9'] + "|       |" + theBoard['u9'] + "|")
print("  |" + theBoard['cm8'] + "|       |" + theBoard['dm8'] + "|       |" + theBoard['um8'] + "|       |" + theBoard['c8'] + "|       |" + theBoard['d8'] + "|       |" + theBoard['u8'] + "|")
print("  |" + theBoard['cm7'] + "|       |" + theBoard['dm7'] + "|       |" + theBoard['um7'] + "|       |" + theBoard['c7'] + "|       |" + theBoard['d7'] + "|       |" + theBoard['u7'] + "|")
print("  |" + theBoard['cm6'] + "|       |" + theBoard['dm6'] + "|       |" + theBoard['um6'] + "|       |" + theBoard['c6'] + "|       |" + theBoard['d6'] + "|       |" + theBoard['u6'] + "|")
print("  |" + theBoard['cm5'] + "|       |" + theBoard['dm5'] + "|       |" + theBoard['um5'] + "|       |" + theBoard['c5'] + "|       |" + theBoard['d5'] + "|       |" + theBoard['u5'] + "|")
print("  |" + theBoard['cm4'] + "|       |" + theBoard['dm4'] + "|       |" + theBoard['um4'] + "|       |" + theBoard['c4'] + "|       |" + theBoard['d4'] + "|       |" + theBoard['u4'] + "|")
print("  |" + theBoard['cm3'] + "|       |" + theBoard['dm3'] + "|       |" + theBoard['um3'] + "|       |" + theBoard['c3'] + "|       |" + theBoard['d3'] + "|       |" + theBoard['u3'] + "|")
print("  |" + theBoard['cm2'] + "|       |" + theBoard['dm2'] + "|       |" + theBoard['um2'] + "|       |" + theBoard['c2'] + "|       |" + theBoard['d2'] + "|       |" + theBoard['u2'] + "|")
print("  |" + theBoard['cm1'] + "|       |" + theBoard['dm1'] + "|       |" + theBoard['um1'] + "|       |" + theBoard['c1'] + "|       |" + theBoard['d1'] + "|       |" + theBoard['u1'] + "|")
print("__+---+_______+---+_______+---+_______+---+_______+---+_______+---+__")
print("|___________________________________________________________________|")

print()

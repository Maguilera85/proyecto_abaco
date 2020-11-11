tablero = {'cm1': '     ' , 'dm1': '   ' , 'um9': '   ' , 'c9': '   ' , 'd9': '   ' , 'u9': '     ' ,
            'cm2': '     ' , 'dm2': '   ' , 'um8': '   ' , 'c8': '   ' , 'd8': '   ' , 'u8': '     ' ,
            'cm3': '     ' , 'dm3': '   ' , 'um7': '   ' , 'c7': '   ' , 'd7': '   ' , 'u7': '     ' , 
            'cm4': '     ' , 'dm4': '   ' , 'um6': '   ' , 'c6': '   ' , 'd6': '   ' , 'u6': '     ' ,
            'cm5': '     ' , 'dm5': '   ' , 'um5': '   ' , 'c5': '   ' , 'd5': '   ' , 'u5': '     ' ,
            'cm6': '     ' , 'dm6': '   ' , 'um4': '   ' , 'c4': '   ' , 'd4': '   ' , 'u4': '     ' ,
            'cm7': '     ' , 'dm7': '   ' , 'um3': '   ' , 'c3': '   ' , 'd3': '   ' , 'u3': '     ' ,
            'cm8': '     ' , 'dm8': '   ' , 'um2': '   ' , 'c2': '   ' , 'd2': '   ' , 'u2': '     ' ,
            'cm9': '     ' , 'dm9': '   ' , 'um1': '   ' , 'c1': '   ' , 'd1': '   ' , 'u1': '     ' }

board_keys = []

for key in tablero:
    board_keys.append(key)
numero_walter = 1

def graficar(numero_walter):
  dicc = dict(enumeroerate(numero_walter))
  valores_lista = len(dicc)
  
  if valores_lista in range(1,6):
    if valores_lista == 1:
        valor_indice_u = dicc[5] # GUARDO LA UNIDAD
        cadena = "X"
        imprimir_pantalla_u = cadena * valor_indice_u
        if tablero['u1'] == '     ':
            tablero['u1'] = imprimir_pantalla_u #IMPRIMO VALOR EN BOARD
    
    
    elif valores_lista == 2:

        valor_indice_d = dicc[4] # GUARDO LA DECENA
        cadena_d = "X"
        imprimir_pantalla_d = cadena_d * valor_indice_d
        if tablero['d1'] == '     ':
            tablero['d1'] = imprimir_pantalla_d #IMPRIMO X EN BOARD
            
        valor_indice_u = dicc[5] # GUARDO LA UNIDAD 
        cadena_u = "X"
        imprimir_pantalla_u = cadena_u * valor_indice_u
        if tablero['u1'] == '     ':
            tablero['u1'] = imprimir_pantalla_u #IMPRIMO X EN BOARD


    elif valores_lista == 3:

        valor_indice_c = dicc[3] # GUARDO LA CENTENA
        cadena_c = "X"
        imprimir_pantalla_c = cadena_c * valor_indice_c # MULTIPLICO X
        if tablero['c1'] == '     ':
           tablero['c1'] = imprimir_pantalla_c #IMPRIMO X EN BOARD
        
        valor_indice_d = dicc[4] # GUARDO LA DECENA
        cadena_d = "X"
        imprimir_pantalla_d = cadena_d * valor_indice_d # MULTIPLICO X 

        if tablero['d1'] == '     ':
            tablero['d1'] = imprimir_pantalla_d #IMPRIMO X EN BOARD
        
        valor_indice_u = dicc[5] # GUARDO LA UNIDAD 
        cadena_u = "X"
        imprimir_pantalla_u = cadena_u * valor_indice_u # MULTIPLICO X

        if tablero['u1'] == '     ':
            tablero['u1'] = imprimir_pantalla_u #IMPRIMO X EN BOARD


    elif valores_lista == 4:

        valor_indice_um = dicc[2] # GUARDO LA UNIDAD DE MIL
        cadena_um = "X"
        imprimir_pantalla_um = cadena_um * valor_indice_um

        if tablero['um1'] == '     ':
           tablero['um1'] = imprimir_pantalla_um #IMPRIMO X EN BOARD

        valor_indice_c = dicc[3] # GUARDO LA CENTENA   
        cadena_c = "X"
        imprimir_pantalla_c = cadena_c * valor_indice_c

        if tablero['c1'] == '     ':
           tablero['c1'] = imprimir_pantalla_c #IMPRIMO X EN BOARD
        
        valor_indice_d = dicc[4] # GUARDO LA DECENA
        cadena_d = "X"
        imprimir_pantalla_d = cadena_d * valor_indice_d

        if tablero['d1'] == '     ':
            tablero['d1'] = imprimir_pantalla_d #IMPRIMO X EN BOARD
            
        valor_indice_u = dicc[5] # GUARDO LA UNIDAD 
        cadena_u = "X"
        imprimir_pantalla_u = cadena_u * valor_indice_u

        if tablero['u1'] == '     ':
            tablero['u1'] = imprimir_pantalla_u #IMPRIMO X EN BOARD


    elif valores_lista == 5:
        valor_indice_dm =  dicc[1] # GUARDO LA DECENA DE MIL
        cadena_dm = "X"
        imprimir_pantalla_dm = cadena_dm * valor_indice_dm

        if tablero['dm1'] == '     ':
            tablero['dm1'] = imprimir_pantalla_dm #IMPRIMO X EN BOARD
        
        valor_indice_um = dicc[2] # GUARDO LA UNIDAD DE MIL
        cadena_um = "X"
        imprimir_pantalla_um = cadena_um * valor_indice_um

        if tablero['um1'] == '     ':
           tablero['um1'] = imprimir_pantalla_um #IMPRIMO X EN BOARD

        valor_indice_c = dicc[3] # GUARDO LA CENTENA   
        cadena_c = "X"
        imprimir_pantalla_c = cadena_c * valor_indice_c

        if tablero['c1'] == '     ':
           tablero['c1'] = imprimir_pantalla_c #IMPRIMO X EN BOARD
        
        valor_indice_d = dicc[4] # GUARDO LA DECENA
        cadena_d = "X"
        imprimir_pantalla_d = cadena_d * valor_indice_d

        if tablero['d1'] == '     ':
            tablero['d1'] = imprimir_pantalla_d #IMPRIMO X EN BOARD
            
        valor_indice_u = dicc[5] # GUARDO LA UNIDAD 
        cadena_u = "X"
        imprimir_pantalla_u = cadena_u * valor_indice_u

        if tablero['u1'] == '     ':
            tablero['u1'] = imprimir_pantalla_u #IMPRIMO X EN BOARD

    elif valores_lista == 6:  
        valor_indice_cm =  dicc[0] # GUARDO LA CENTENA DE MIL
        cadena_cm = "X"
        imprimir_pantalla_cm = cadena_cm * valor_indice_cm

        if tablero['cm1'] == '     ':
            tablero['cm1'] = imprimir_pantalla_cm #IMPRIMO X EN BOARD

        valor_indice_dm =  dicc[1] # GUARDO LA DECENA DE MIL
        cadena_dm = "X"
        imprimir_pantalla_dm = cadena_dm * valor_indice_dm

        if tablero['dm1'] == '     ':
            tablero['dm1'] = imprimir_pantalla_dm #IMPRIMO X EN BOARD
        
        valor_indice_um = dicc[2] # GUARDO LA UNIDAD DE MIL
        cadena_um = "X"
        imprimir_pantalla_um = cadena_um * valor_indice_um

        if tablero['um1'] == '     ':
           tablero['um1'] = imprimir_pantalla_um #IMPRIMO X EN BOARD

        valor_indice_c = dicc[3] # GUARDO LA CENTENA   
        cadena_c = "X"
        imprimir_pantalla_c = cadena_c * valor_indice_c

        if tablero['c1'] == '     ':
           tablero['c1'] = imprimir_pantalla_c #IMPRIMO X EN BOARD
        
        valor_indice_d = dicc[4] # GUARDO LA DECENA
        cadena_d = "X"
        imprimir_pantalla_d = cadena_d * valor_indice_d

        if tablero['d1'] == '     ':
            tablero['d1'] = imprimir_pantalla_d #IMPRIMO X EN BOARD
            
        valor_indice_u = dicc[5] # GUARDO LA UNIDAD 
        cadena_u = "X"
        imprimir_pantalla_u = cadena_u * valor_indice_u

        if tablero['u1'] == '     ':
            tablero['u1'] = imprimir_pantalla_u #IMPRIMO X EN BOARD
  else:
    print("error")

  """– 1 unidad = 1 unidad
    – 1 decena = 10 unidades
    – 1 centena = 100 unidades
    – 1 unidad de mil = 1 000 unidades
    – 1 decena de mil = 10 000 unidades
    – 1 centena de mil = 100 000 unidades """

    
import re
import pandas as pd
import openpyxl 

#Metodos
def leer_libro(path):
    return pd.read_excel(path)

def estado_incial(libro):
    return libro['Estados'].values[0]

def dame_lista_estados(libro):
    return list(libro['Estados'].values)

def filtrar_aceptadores(libro):
    return libro[libro['Aceptador'] == "si"]

def filtrar_no_aceptadores(libro):
    return libro[libro['Aceptador'] == "no"]

def construir_diccionario(estados, libro):
    diccionario_estados = {}
    for i in range(len(estados)):
            dic = { "a" : libro['A'].values[i] , "b" : libro['B'].values[i] }
            diccionario_estados[libro['Estados'].values[i]] = dic
    return diccionario_estados

def validacion_cadena(cadena):
    regex_cadena = re.compile(r"[a-b]*")
    return re.fullmatch(regex_cadena, cadena)


#MAIN
def main():
    libro = leer_libro("./prueba.xlsx")

    estado = estado_incial(libro) #estado inicial

    estados = dame_lista_estados(libro)

    
    cadena = input("Ingrese cadena a validar: ") 
    if validacion_cadena(cadena): 
        print(f"'{cadena}' Es valida!") 
    else: 
        print(f"'{cadena}'No es valida!") 

    # regex_estado = re.compile(r"[s-0-9]*") 
    # estado = input("Ingrese cadena a validar: ") 

    # if re.fullmatch(regex_estado, estado): 
    #     print(f"'{estado}' Es valido!") 
    # else: 
    #     print(f"'{estado}'No es valido!") 

    diccionario_estados = construir_diccionario(estados,libro)

    filtro_aceptadores= filtrar_aceptadores(libro)
    filtro_no_aceptadores = filtrar_no_aceptadores(libro)
    estados_aceptadores = list(filtro_aceptadores['Estados'])
    estados_no_aceptadores = list(filtro_no_aceptadores['Estados'])

    for caracter in cadena:
        if estado == "B":
            break
        val_estado=diccionario_estados[estado]
        print(f"Caminos posibles:{val_estado}")
        estado=val_estado[caracter]
        print(f"Me voy por estado:{estado}")
    
    if(estado in estados_aceptadores):   
        print("el automata acepta la cadena")
    else:
        print("el automata no acepta la cadena")


if __name__ == "__main__":
    main()
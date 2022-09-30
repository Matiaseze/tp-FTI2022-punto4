import re
import pandas as pd

#Metodos
def leer_libro(path): #Lee el archivo
    return pd.read_excel(path)

def estado_incial(libro): #Devuelve el primer estado que ese va a ser el inicial
    return libro["Estados"].values[0]

def dame_lista_estados(libro):#devuelve los estados en una lista
    return list(libro["Estados"].values)

def filtrar_aceptadores(libro):#filtra por estados aceptadores
    return libro[libro["Aceptador"] == "si"]

def construir_diccionario(estados, libro):#crea un diccionario de diccionarios para recorrer el automata
    diccionario_estados = {}
    for i in range(len(estados)):
            dic = { 'a' : libro['A'].values[i] , 'b' : libro['B'].values[i] }
            diccionario_estados[libro["Estados"].values[i]] = dic
    return diccionario_estados

def validacion_cadena(cadena): #valida la entrada de texto
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
    
        diccionario_estados = construir_diccionario(estados,libro)

        filtro_aceptadores= filtrar_aceptadores(libro)
        estados_aceptadores = list(filtro_aceptadores['Estados'])

        for caracter in cadena:
            if estado == "B": # = estado basura
                break # si llega al estado basura termina ejecucion
            val_estado=diccionario_estados[estado]
            print(f"Caminos posibles:{val_estado}") # muestro los caminos segun el estado
            estado=val_estado[caracter]
            print(f"Me voy por estado:{estado}") #muestro el estado al que voy
        
        if(estado in estados_aceptadores):   
            print("el automata acepta la cadena")
        else:
            print("el automata no acepta la cadena")    
    else: 
        print(f"'{cadena}'No es valida!") 

if __name__ == "__main__":
    main()
import re
import pandas as pd
import openpyxl 

book = openpyxl.load_workbook('prueba.xlsx', data_only=True) #archivo el cual quiero leer

hoja = book.active # para fijar la hoja
#['A1' : 'C5'] rango de celdas que quiero que lea
valores = hoja ['A1' : 'C1']  #fila de valores a|b
estados = hoja ['A2' : 'A5']  #columna de estados s0,s1,s2,s3
estadoDeAB = hoja ['B2' : 'C5']

# estados = [] # estados de la tabla
# for fila in celdas: # lee primero A1 A2 A3 A4 ... B1 B2 B3 B4 ...
#     estados =  [celda.value for celda in fila] #leo el valor de la celda de la fila y lo guardo en "estados"
#     print (estados)

lista = []
lista2 = []
 
# diccionario = {}

# for estado in estados:
#     var1 = [valor.value for valor in estado]
#     lista.append(var1)
# print(lista)

# for estado2 in estadoDeAB:
#     var2 = [valor.value for valor in estado2]
#     lista2.append(var2)
# print(lista2)

for estado in estados:
    var1 = [valor.value for valor in estado]
    print(var1)
    for estado2 in estadoDeAB:
        var2 = [valor.value for valor in estado2]
        print(var2)



# estados={"s0":{"a":"s0","b":"s1"},"s1":{"a":"s1","b":"s2"},"s2":{"a":"s2","b":"s3"}} tratar de llegar a este resultado
# lista2 = dict(lista2)
# prueba = dict(zip(lista,lista2))

# resultado = [ dict(zip(lista2, i)) for i in lista ]
# print(resultado)
# diccionario = {}
# for i in range(len(lista2)):
#   diccionario[lista2[i]] = lista[i]

# print(diccionario)

user_keys = ['s', 'lastName']
users = [
  ['1043100330', 'Smith'], 
  ['1043100331', 'Swartz'], 
  ['1043100332', 'Laff']]

resultado = [ dict(zip(user_keys, i)) for i in users ]
# print(resultado)





# estados={"e0":{"a":"e0","b":"e1"},"e1":{"a":"e1","b":"e2"},"e2":{"a":"e2","b":"e3"}}
# cadena=["a","a","b","a","b","b"]
# valores=list(estados.values())
# print(valores)
# estado="e0"

# while estado != "e3":
#     estado=estados[estado]
#     print(f"estas en:{estado}")
#     estado=estado[cadena.pop()]

# print("legaste a un estado terminal rey")
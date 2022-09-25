import re
import pandas as pd
import openpyxl 

book = openpyxl.load_workbook('prueba.xlsx', data_only=True)

hoja = book.active

celdas = hoja ['A1' : 'B1' : 'C1']

for fila in celdas: 

    print ([celda.value for celda in fila])


estados={"e0":{"a":"e0","b":"e1"},"e1":{"a":"e1","b":"e2"},"e2":{"a":"e2","b":"e3"}}
cadena=["a","a","b","a","b","b"]
valores=list(estados.values())
print(valores)
estado="e0"

while estado != "e3":
    estado=estados[estado]
    print(f"estas en:{estado}")
    estado=estado[cadena.pop()]

print("legaste a un estado terminal rey")
import re
import pandas as pd
import openpyxl 
from openpyxl import Workbook

book = openpyxl.load_workbook('prueba.xlsx')
sheet = book.active
a=sheet['B1'].value
b=sheet['C1'].value
s0=sheet['A2'].value
s1=sheet['A3'].value
s2=sheet['A4'].value
s3=sheet['A5'].value

cadena = [b,b]
 
estados={s0:{a:s0,b:s1},s1:{a:s1,b:s2},s2:{a:s2,b:s3},s3:{a:s3,b:s3}}

valores=list(estados.values())
print(valores)
estado=s0
print(len(cadena))
for caracter in cadena:
    estado=estados[estado]
    print(f"estas en:{estado}")
    estado=estado[caracter]
if(estado == s1 or estado == s3):   
    print("el automata acepta la cadena")
else:
    print("el automata no acepta la cadena")

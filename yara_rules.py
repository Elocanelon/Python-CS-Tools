import yara
import os

directorio = "" #Directorio de los archivos que queremos analizar 
yara_rules = yara.compile(filepath = "/foo/bar/myrules.yar") #Archivo con las reglas yaras a usar 

for filename in os.listdir(directorio):
    matches = yara_rules.match(data=filename)
    if matches:
        print(filename + ": Coincide con scaneo, posiblemente infectado")
    else: 
        print(filename + ": Limpio")    
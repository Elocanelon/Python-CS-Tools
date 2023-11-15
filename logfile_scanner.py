

def openLogFile(path):  
    with open(path) as log_file:  #Abrimos el archivo log
        for log_entry in log_file:     #Separamos cada una de los logs 
            yield log_entry                 #Retornamos cada uno de los logs dentro de la funcion 
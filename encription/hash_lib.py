import hashlib

message = int(input("Seleccione el tipo de encriptacion que quiere usar: \n 1.- sha256 \n 2.- md5 \n"))

#Opcion sha256 
if message == 1:
        str = input("Ingrese el valor a encriptar: ")
        str = str.encode()
        result = hashlib.sha256(str)
        print("El valor encriptado es: ", result.hexdigest())

#Opcion md5
if message == 2:
        str = input("Ingrese el valor a encriptar: ")
        str = str.encode()
        result = hashlib.md5(str)
        print("El valor encriptado es: ", result.hexdigest())

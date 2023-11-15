import base64

#Primera parte 
statement = int(input("Por favor seleccione la opcion si quiere encriptar o desencriptar \n 1.- Encriptar texto \n 2.- Desencriptar texto \n"))


#Encriptar
if statement == 1:
    message = input("Por favor ingrese el valor a encriptar: \n")
    mbytes = message.encode()
    base64_bytes = base64.b64encode(mbytes)
    base64_encoded = base64_bytes.decode()
    print("Encriptacion base64: " + base64_encoded)
#Desencriptar 
elif statement == 2:
    try:
        message = input("Por favor ingrese el valor a desencriptar: \n")
        message_bytes = base64.b64decode(message)
        statement_decoded = message_bytes.decode()
        print("Desencriptacion base64: " + statement_decoded)
    except Exception as e:
        print("Error al desencriptar :", str(message))


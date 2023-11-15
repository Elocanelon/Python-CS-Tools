from cryptography.fernet import Fernet

f_key = Fernet.generate_key()
print("Key: " + str(f_key))
f_enc = Fernet(f_key)

passwd = input("Ingresa la clave que se quiera encriptar: ")
enc_string = f_enc.encrypt(passwd.encode())

print("Encriptacion: " + str(enc_string))

#print("Desencriptacion: " + str(f_enc.descypt(enc_string)))
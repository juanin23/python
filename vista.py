import control as ct

print("Probando entrada y salida estandar\nIngresa tu nombre y presiona enter")
nombre = ct.nombre()
print("Ingresa tu edad y presiona enter")
edad = ct.edad()
print("\nBienvenido " , nombre)
print("Tu edad es: " , edad)
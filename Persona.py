class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

alan = Persona("Alan", 28)

print(alan.nombre)
print(alan.edad)
print(type(alan))
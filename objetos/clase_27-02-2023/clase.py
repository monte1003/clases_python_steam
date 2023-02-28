class Persona():
    nombre = "Isaac"
    edad = 14
    def caminar(self):
        print(self.nombre, "esta caminando")
        
p1 = Persona()
print(p1.nombre)

class Practica():
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        print(f"{self.nombre} tiene {self.edad} años")

p1 = Practica("Isaac","12")
print(p1.nombre)
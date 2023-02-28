class Robot():
    x = 0
    y = 0
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        
    def arriba(self):
        eje_y = float(input('Cuanto avanzaste en el eje y: '))
        self.y = self.y + eje_y
    
    def abajo(self):
        eje_y = float(input('Cuanto bajaste en el eje y: '))
        self.y = self.y - eje_y
        
    def derecha(self):
        eje_x = float(input('Cuanto avanzaste en el eje x: '))
        self.x = self.x + eje_x
        
    def izquierda(self):
        eje_x = float(input('Cuanto disminuiste en el eje x: '))
        self.x = self.x + eje_x
    
    def posicion(self):
        print(f"Posición x {self.x}")
        print(f"Posición y {self.y}")
    
    
robotsi = Robot("pepe")
menu = """
\t\t\t\t\t\tBienvenido a ROBOTSI
1 para avanzar en y
2 para disminuir en y
3 para avanzar en x
4 para disminuir en x
5 paraa mos
"""
print(menu)
while True:
    opcion = int(input("Introduce tu opción: "))
    match opcion:
        case 1:
            robotsi.arriba()
        case 2:
            robotsi.abajo()
        case 3:
            robotsi.derecha()
        case 4:
            robotsi.izquierda()
        case 5:
            break

robotsi.posicion()
    
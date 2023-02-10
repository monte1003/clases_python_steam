#  FORMA 1: from function import area_rectangulo
# area_rectangulo()

#Forma 2: import function
#Forma 2: function.area_rectangulo()

from importando_funciones.function import area_rectangulo
if __name__ == '__main__':
    base:float = float(input('Introduce la base del rectangulo: '))
    altura:float = float(input('Introduce la altura del rectangulo: '))
    result:float = area_rectangulo(base,altura)
    print(f'El área del rectángulo es {result}')
    
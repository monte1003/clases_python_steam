#  FORMA 1: from function import area_rectangulo
# area_rectangulo()

#Forma 2: import function
#Forma 2: function.area_rectangulo()

from function import area_rectangulo
base:float = float(input('Introduce la base del rectangulo: '))
altura:float = float(input('Introduce la altura del rectangulo: '))
result = area_rectangulo(base,altura)
print(result)
import math
def calcular_distancias(
    x_1:float,
    x_2:float,
    y_1:float,
    y_2:float
    
) -> float:
    """
    Función que calcula la distancia entre 2 puntos
    ---params---
    - x_1(float): Valor de partida lado 1
    - x_2(float): Valor de partida lado 2
    - y_1(float): Distancia que hay entre punto 1 y punto 2
    - y_2(float): Distancia (2) que hay entre punto 1 y punto 2
    ---return---
    
    """
    x = math.pow(x_2-x_1,2)
    y = math.pow(y_2 - y_1,2)
    d = math.sqrt(x-y)
    return d
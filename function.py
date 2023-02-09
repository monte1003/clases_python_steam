def area_rectangulo(
    x:float,
    y:float
) -> float:
    """
    Función que calcula el área de un rectangulo
    ---params---
    - x(float): Base del Rectángulo
    - y(float): Altura del Rectángulo 
    
    ---return---
    area (float): Area de mi rectangulo
    """
    area = x * y
    return area
    
    base:float = float(input('Introduce la base del rectangulo: '))
    altura:float = float(input('Introduce la altura del rectangulo: '))
    result = area_rectangulo(base,altura)
    print(f'El área del cuadrado es {result}')

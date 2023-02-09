from funciones_bibliotecas import crear
usuarios = {}
menu = """
\t      Biblioteca Karl Parris.J:
\t  Presiona 1 para Agregar
"""
print(menu)
opcion:int = int(input('Ingresa una opción: '))
try:
    match opcion:
        case 1:
            n:str = str(input('Ingresa tu nombre y tu apellido: '))
            e:int = int(input('Ingresa tu edad: '))
            result = crear(n,e,usuarios)
except ValueError:
    print('Los datos ingresados no son válidos')
print(result)
        
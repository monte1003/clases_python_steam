from funcion_crear import crear
from funcion_eliminar import eliminar
usuarios = {}
while True:
    menu = """
    \t                    Biblioteca Karl Parris.J:
    \t  Presiona 1 para Agregar
    """
    print(menu)
    opcion:int = int(input('Ingresa una opción: '))
    print(usuarios)
    match opcion:
        case 1:
            n:str = str(input('Ingresa tu nombre y tu apellido: '))
            n.title()
            e:str = str(input('Ingresa el nombre del libro que prestaste: '))
            crear(n,e,usuarios)
    n = input('')
    if n == '0':
        print(usuarios)
        break
        
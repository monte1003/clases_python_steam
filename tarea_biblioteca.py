from funcion_crear import crear
from funcion_eliminar import eliminar
usuarios = {}
while True:
    menu = """
    \t                    Biblioteca Karl Parris.J:
    \t  Presiona 1 para Agregar Usuario
    \t  Presiona 2 para Eliminar Usuario
    \t  Presiona 3 para Actualizar Libro que 
    """
    print(menu)
    opcion:int = int(input('Ingresa una opción: '))
    match opcion:
        case 1:
            n:str = str(input('\nIngresa tu nombre y tu apellido: '))
            n.title()
            e:str = str(input('Ingresa el nombre del libro que prestaste: '))
            crear(n,e,usuarios)
            n = input('Presiona cualquier tecla para reiniciar o 0 para finalizar')
            if n == '0':
                break
        case 2:
            n = str(input('\nIngresa el nombre del usuario que deseas eliminar: '))
            eliminar(n,usuarios)
            n = input('Presiona cualquier tecla para reiniciar o 0 para finalizar')
            if n == '0':
                break
print(usuarios)
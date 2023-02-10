import os
from funcion_crear import crear
from funcion_eliminar import eliminar
from actualizar import actualizar_usuario
from visualizar import visualizar_usuarios
usuarios = {}
while True:
    menu = """
    \t                    Biblioteca Karl Parris.J:
    \t  Presiona 1 para Agregar Usuario
    \t  Presiona 2 para Eliminar Usuario
    \t  Presiona 3 para Actualizar Libro que Presto el Usuario
    \t  Presiona 4 para Visualizar la base de datos
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
        case 3:
            nombre:str = str(input('Ingresa el nombre del usuario que va a prestar el nuevo libro: '))
            libro:str = str(input(f'Ingresa el nuevo libro que presto el usuario {nombre}: '))
            visualizar_usuarios(nombre,libro,usuarios)
            n = input('Presiona cualquier tecla para reiniciar o 0 para finalizar')
            if n == '0':
                break
        case 4:
            n:str = str(input('Ingresa el nombre del cual desea saber el libro prestado: '))
            e:str = str(input('Ingresa el libro que tiene el usuario: '))
            actualizar_usuario(n,e,usuarios)
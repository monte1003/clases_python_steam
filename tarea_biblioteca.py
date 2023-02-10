import os
from funcion_crear import crear
from funcion_eliminar import eliminar
from actualizar import actualizar_usuario
from visualizar import visualizar_usuarios
from visualizar_2 import visualizar_total
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
    os.system('cls')
    match opcion:
        case 1:
            print('\t\t\tAgregar Usuario')
            n:str = str(input('\nIngresa tu nombre y tu apellido: '))
            n.title()
            e:str = str(input('Ingresa el nombre del libro que prestaste: '))
            crear(n,e,usuarios)
            n = input('Presiona cualquier tecla para continuar ')
            os.system('cls')
            if n == '0':
                break
        case 2:
            print('\t\t\tEliminar Usuario')
            n = str(input('\nIngresa el nombre del usuario que deseas eliminar: '))
            eliminar(n,usuarios)
            n = input('Presiona cualquier tecla para reiniciar o 0 para finalizar')
            os.system('cls')
            if n == '0':
                break
        case 3:
            print('\t\t\tActualizar Usuario')
            nombre:str = str(input('Ingresa el nombre del usuario que va a prestar el nuevo libro: '))
            libro:str = str(input(f'Ingresa el nuevo libro que presto el usuario {nombre}: '))
            actualizar_usuario(nombre,libro, usuarios)
            n = input('Presiona cualquier tecla para reiniciar o 0 para finalizar')
            os.system('cls')
            if n == '0':
                break
        case 4:
            print('\t\t\tVisualizar Usuarios')
            n = """
            Presiona 1 para visualizar a un usuario en específico
            Presiona 2 para visualizar toda la base de datos
            """
            print(n)
            op = input('\n\tSelecciona una opcion: ')
            if op == '1':
                n = str(input('Introduce el nombre del usuario el cual deseas ver su información: '))
                visualizar_usuarios(n,usuarios)
            elif op == '2':
                visualizar_total(usuarios)
            n = input('Presiona cualquier tecla para reiniciar o 0 para finalizar')
            os.system('cls')

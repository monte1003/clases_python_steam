import os
from proyecto_biblioteca.funciones.funcion_crear import crear
from proyecto_biblioteca.funciones.funcion_eliminar import eliminar
from proyecto_biblioteca.funciones.actualizar import actualizar_usuario
from proyecto_biblioteca.funciones.visualizar import visualizar_usuarios
from proyecto_biblioteca.funciones.visualizar_2 import visualizar_total
usuarios = {}
while True:
    menu = """
    \t\t\t\t\t\t\t\t                    Biblioteca Karl Parris.J:
    \n\t  Presiona 1 para Agregar Usuario
    \t  Presiona 2 para Eliminar Usuario
    \t  Presiona 3 para Actualizar Libro que Presto el Usuario
    \t  Presiona 4 para Visualizar la base de datos
    \t  Presiona 5 para salir del Programa
    """
    print(menu)
    opcion:int = int(input('Ingresa una opción: '))
    os.system('cls')
    match opcion:
        case 1:
            print('\t\t\t\t\t\t\t\tAgregar Usuario')
            n:str = str(input('\nIngresa el nombre y apellido del usuario: '))
            n.title()
            e:str = str(input('Ingresa el nombre del libro a prestar del usuario: '))
            crear(n,e,usuarios)
            os.system('cls')
        case 2:
            print('\t\t\t\t\t\t\t\tEliminar Usuario')
            n = str(input('\nIngresa el nombre del usuario que deseas eliminar: '))
            n.title()
            eliminar(n,usuarios)
            os.system('cls')
        case 3:
            print('\t\t\t\t\t\t\t\tActualizar Usuario')
            nombre:str = str(input('\nIngresa el nombre del usuario que va a prestar el nuevo libro: '))
            n.title
            libro:str = str(input(f'Ingresa el nuevo libro que presto el usuario {nombre}: '))
            actualizar_usuario(nombre,libro, usuarios)
            os.system('cls')
        case 4:
            print('\t\t\t\t\t\t\t\tVisualizar Usuarios')
            n = """
            Presiona 1 para visualizar a un usuario en específico
            Presiona 2 para visualizar toda la base de datos
            """
            print(n)
            op = input('\n\tSelecciona una opcion: ')
            if op == '1':
                n = str(input('\nIntroduce el nombre del usuario el cual deseas ver su información: '))
                n.title()
                visualizar_usuarios(n,usuarios)
            elif op == '2':
                visualizar_total(usuarios)
        case 5:
            break
print('\nFIN DEL PROGRAMA')

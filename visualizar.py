def visualizar_usuarios(
    persona:str,
    libro: str,
    diccionario:dict
) -> dict:
    print("""
        \n\nPara visualizar la base de datos seleccione:
        \nPresiona 1 para visualizar un usuario en específico
        \nPresione 2 para visualizar toda la base de datos
        """)
    n = int(input('Opcion: '))
    match n:
        case 1:
            print(f'El usuario {diccionario[persona]} tiene el libro {libro}')
        case 2:
            print(diccionario)
def visualizar_usuarios(
    persona:str,
    diccionario:dict
) -> dict:
    print(f'El usuario {persona} tiene el libro {diccionario[persona]}')
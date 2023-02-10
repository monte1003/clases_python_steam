def actualizar_usuario(
    usuario:str,
    libro:str,
    diccionario:dict
) -> dict:
    diccionario[usuario] = libro
    return diccionario

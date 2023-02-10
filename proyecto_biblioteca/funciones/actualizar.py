def actualizar_usuario(
    usuario:str,
    libro:str,
    diccionario:dict
) -> dict:
    """
        Función que actualiza el libro que presto el usuario
    
    ----Argumentos----:
    
        usuario (str): Nombre del usuario el cual deseamos actualizar el libro que prestó
        libro (str): Libro nuevo que presto el usuario (ACTUALIZADO)
        diccionario (dict): diccionario al cual se va a actualizar ese valor

    ----Retorno----:
    
        dict: Devuelve el diccionario con el valor actualizado (el libro que pasamos como parámetro)
    """
    usuario.title()
    diccionario[usuario] = libro
    return diccionario

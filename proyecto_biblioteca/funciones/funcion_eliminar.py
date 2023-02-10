
def eliminar(
    nombre:str,
    diccionario:dict
) -> dict:
    """
    Función que elimina a un usuario y su información del diccionario

    ----Argumentos----:
    
        nombre (str): Nombre del usuario el cual queremos eliminar del diccionari
        diccionario (dict): Nombre del diccionario del cual eliminaremos la información del usuario

    ----Retorno----:

        Retorna el mismo diccionario pero con el usuario y su información seleccionado eliminado
        
        
    """
    nombre = nombre.title()
    diccionario.pop(nombre)
    return diccionario
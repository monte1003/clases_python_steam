def crear(
    nombre:str,
    libro:str,
    diccionario:dict
) -> dict:
    """
        Función que consiste en crear un usuario en nuestro diccionario cuya "key" sea el nombre del usuario y el "value" será el libro que presto

    ----Argumentos----:
    
        nombre (str):El nombre del usuario
        libro (str): Nombre del libro que presto el usuario
        diccionario (dict): Nombre del diccionario al cual se van a añadir esos valores

    ----Retorno----:
    
        dict: Devuelve el diccionario con el usuario creado
    """
    nombre.title()
    diccionario.update({nombre:libro})
    return diccionario


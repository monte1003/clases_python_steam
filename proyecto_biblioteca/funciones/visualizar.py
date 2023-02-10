def visualizar_usuarios(
    persona:str,
    diccionario:dict
) -> dict:
    """
        Función que consiste en visualizar los usuarios en un diccionario

    ----Argumentos----:
        
        persona (str):El nombre de la persona (la key en mi diccionario)
        diccionario (dict): nombre de nuestro diccionario

    ----Retorno----:
        
        dict: Devuelve el nombre de la persona y el valor accediendo a su valor por medio de la clave "persona" en nuestro diccionario
    """
    persona = persona.title()
    print(f'\nEl usuario {persona} tiene el libro {diccionario[persona]}')
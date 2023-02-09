def crear(
    nombre:str,
    libro:str,
    diccionario:dict
) -> dict:
        diccionario.update({nombre:libro})
        return diccionario


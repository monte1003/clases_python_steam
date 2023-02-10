
def eliminar(
    nombre:str,
    diccionario:dict
) -> dict:
        diccionario.pop(nombre)
        return diccionario
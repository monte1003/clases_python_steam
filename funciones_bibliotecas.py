def crear(
    nombre:str,
    libro:str,
    diccionario:dict
) -> dict:
        diccionario.update({'Nombre':nombre,'Libro Prestado':libro})
        return diccionario


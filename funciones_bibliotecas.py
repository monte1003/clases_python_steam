def crear(
    nombre:str,
    libro:str,
    diccionario:dict
) -> dict:
        diccionario = dict.update({'Nombre':nombre,'Libro Prestado':libro})
        return diccionario


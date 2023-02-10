def visualizar_total(
    diccionario:dict
) -> dict:
    for key,value in diccionario.items():
        print(f'El usuario {key} tiene el libro {value}')
import time
def visualizar_total(
    diccionario:dict
) -> dict:
    """
        Función que con ciclo for recorre el diccionario e imprime esos valores con un "delay" de 1 segundo

    ----Argumentos----:

        diccionario (dict): Le pasamos el nombre del diccionario que queremos recorrer

    ----Retorno:
    
        dict: La función devuelve una línea de código que te dice el nombre del usuario y que libro tiene prestado
    """
    for key,value in diccionario.items():
        print(f'El usuario {key} tiene el libro {value}')
        time.sleep(1)
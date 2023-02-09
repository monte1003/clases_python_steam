def mayor_edad(edad:int) -> bool:
    if edad<18:
        return 0
    return 1

def crear_lista(n:int) -> list:
    lista = []
    for i in range(n):
        lista.append(i+1)
    return lista
n = int(input('Ingresa un número: '))
result = crear_lista(n)
print(result)
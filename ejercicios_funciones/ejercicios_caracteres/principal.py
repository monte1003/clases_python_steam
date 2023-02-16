from funcion_caracteres import palabra
palabra_2 = str(input('Introduce una frase: '))
lista = palabra(palabra_2)
print(lista)
print('\n')
total = 0
for i in range(len(lista)):
    print(f'La palabra {lista[i]} tiene {len(lista[i])} caracteres')
    total += len(lista[i])
print(f'\nEl total de caracteres de la frase o palabra es {total} caracteres')

def BusquedaBinaria(lista, principio, ultimo, n):
    if principio > ultimo:
        return False
    mitad = (principio + ultimo) // 2
    if lista[mitad] == n:
        return True
    elif lista[mitad] < n:
        return BusquedaBinaria(lista, mitad + 1, ultimo, n)
    else:
        return BusquedaBinaria(lista, principio, mitad - 1, n)

lista = [1,2,4,6,7,8,9,15,20,25]
n = int(input('Ingresa el elemento que deseas encontrar: '))
print(lista)
encontrado = BusquedaBinaria(lista, 0, len(lista), n)
print(f'El elemento {n} {"está" if encontrado else "no está"} en la lista')
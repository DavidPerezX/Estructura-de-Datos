#DPX
def BucketSort(lista):
    mayor = max(lista)
    longitud = len(lista)
    tamaño = mayor / longitud

    buckets = [[] for _ in range(longitud)]
    for i in range(longitud):
        j = int(lista[i] / tamaño)
        if j != longitud:
            buckets[j].append(lista[i])
        else:
            buckets[longitud - 1].append(lista[i])

    for i in range(longitud):
        Ordenar(buckets[i])

    resultado = []
    for i in range(longitud):
        resultado = resultado + buckets[i]

    return resultado


def Ordenar(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i - 1
        while (j >= 0 and aux < lista[j]):
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = aux

lista = [3,4,5,2,1,22,2,0,145]
listaOrdenada = BucketSort(lista)
print(f"Lista en desorden: {lista}")
print(f"Lista ordenada: {listaOrdenada}")
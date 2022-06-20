class Grafo:
    def __init__(self,grafodic=None):
        if grafodic is None:
            grafodic ={}
        self.grafodic = grafodic

    def agregarArista(self,vertice,arista):
        self.grafo[vertice].append(arista)

Prueba = { "a" : ["b","c"],"b" : ["a", "e"],"c" : ["b", "e", "f"], "d" : ["c", "f", "e"],"e" : ["d", "f"]
               }
grafito = Grafo(Prueba)
print(grafito.grafodic)

Adyacencia = {}
with open("C:\\Users\\David\\Documents\\graf.txt", "r") as archivo :
    for linea in archivo:
        dividir = linea.split()
        Adyacencia.setdefault(dividir[0],[]).append(dividir[1])

print(Adyacencia)
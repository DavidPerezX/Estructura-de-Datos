#DPX
class ArbolBinario:
    def __init__(self, tamaño):
        self.Lista = tamaño * [None]
        self.UltimoIndiceUsado = 0
        self.tamañoMax = tamaño
    
    def AgregarNodo(self, valor):
        if self.UltimoIndiceUsado + 1 == self.tamañoMax:
            return "El arbol está lleno"
        self.Lista[self.UltimoIndiceUsado+1] = valor
        self.UltimoIndiceUsado += 1
        return "Valor añadido"

    def BuscarNodo(self, ValorNodo):
        for i in range(len(self.Lista)):
            if self.Lista[i] == ValorNodo:
                return "Encontrado"
        return "No encontrado"
    
    def preorden(self, indice):
        if indice > self.UltimoIndiceUsado:
            return
        print(self.Lista[indice])
        self.preorden(indice*2)
        self.preorden(indice*2 + 1)

    def enOrden(self, indice):
        if indice > self.UltimoIndiceUsado:
            return
        self.enOrden(indice* 2)
        print(self.Lista[indice])
        self.enOrden(indice*2 + 1)
    
    def postOrden(self, indice):
        if indice > self.UltimoIndiceUsado:
            return
        self.postOrden(indice * 2)
        self.postOrden(indice* 2 + 1)
        print(self.Lista[indice])
    
    def BorrarNodo(self, valor):
        if self.UltimoIndiceUsado == 0:
            return "No hay ningún nodo"
        for i in range(1, self.UltimoIndiceUsado+1):
            if self.Lista[i] == valor:
                self.Lista[i] = self.Lista[self.UltimoIndiceUsado]
                self.Lista[self.UltimoIndiceUsado] = None
                self.UltimoIndiceUsado -= 1
                return "El nodo ha sido borrado"
        else:
            return "No existe ese nodo"
    
    def BorrarArbol(self):
       self.Lista = None
       return "El arbol ha sido eliminado"

    
 

NuevoArbol = ArbolBinario(8)
NuevoArbol.AgregarNodo("Disney")
print(NuevoArbol.AgregarNodo("Hulu"))
NuevoArbol.AgregarNodo("hbo")
NuevoArbol.AgregarNodo("netflix")
NuevoArbol.enOrden(1)
print(NuevoArbol.BorrarNodo("clarovideo"))
NuevoArbol.enOrden(1)
print(NuevoArbol.BorrarNodo("hbo"))
NuevoArbol.enOrden(1)

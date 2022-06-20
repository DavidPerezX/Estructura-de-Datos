
class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
    
    def __str__(self):
        return str(self.valor)

class ListaLigada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
class Cola:
    def __init__(self):
        self.ListaLigada = ListaLigada()
    
    def __str__(self):
        valor = [str(x) for x in self.ListaLigada]
        return ' '.join(valor)
    
    def enCola(self, valor):
        NuevoNodo = Nodo(valor)
        if self.ListaLigada.cabeza == None:
            self.ListaLigada.cabeza = NuevoNodo
            self.ListaLigada.cola = NuevoNodo
        else:
            self.ListaLigada.cola.siguiente = NuevoNodo
            self.ListaLigada.cola = NuevoNodo
    
    def Vacio(self):
        if self.ListaLigada.cabeza == None:
            return True
        else:
            return False
    
    def SacarCola(self):
        if self.Vacio():
            return 
        else:
            NodoTemporal = self.ListaLigada.cabeza
            if self.ListaLigada.cabeza == self.ListaLigada.cola:
                self.ListaLigada.cabeza = None
                self.ListaLigada.cola = None
            else:
                self.ListaLigada.cabeza = self.ListaLigada.cabeza.siguiente
            return NodoTemporal
    
    def borrar(self):
        self.ListaLigada.cabeza = None
        self.ListaLigada.cola = None


class ArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.hijoIzq = None
        self.hijoDer = None

def AgregaNodo(NodoRaiz, nodevalor):
    if NodoRaiz.valor == None:
        NodoRaiz.valor = nodevalor
    elif nodevalor <= NodoRaiz.valor:
        if NodoRaiz.hijoIzq is None:
            NodoRaiz.hijoIzq = ArbolBinario(nodevalor)
        else:
            AgregaNodo(NodoRaiz.hijoIzq, nodevalor)
    else:
        if NodoRaiz.hijoDer is None:
            NodoRaiz.hijoDer = ArbolBinario(nodevalor)
        else:
            AgregaNodo(NodoRaiz.hijoDer, nodevalor)
    return "Nodo insertado"

def RecorridoPreOrden(NodoRaiz):
    if not NodoRaiz:
        return
    print(NodoRaiz.valor,end=" ")
    RecorridoPreOrden(NodoRaiz.hijoIzq)
    RecorridoPreOrden(NodoRaiz.hijoDer)

def RecorridoEnOrden(NodoRaiz):
    if not NodoRaiz:
        return
    RecorridoEnOrden(NodoRaiz.hijoIzq)
    print(NodoRaiz.valor,end=" ")
    RecorridoEnOrden(NodoRaiz.hijoDer)

def RecorridoPostOrden(NodoRaiz):
    if not NodoRaiz:
        return
    RecorridoPostOrden(NodoRaiz.hijoIzq)
    RecorridoPostOrden(NodoRaiz.hijoDer)
    print(NodoRaiz.valor,end=" ")
            
def BuscarNodo(NodoRaiz, nodevalor):
    if NodoRaiz.valor == nodevalor:
        print("Valor encontrado")
    elif nodevalor < NodoRaiz.valor:
        if NodoRaiz.hijoIzq.valor == nodevalor:
            print("Valor encontrado")
        else:
            BuscarNodo(NodoRaiz.hijoIzq, nodevalor)
    else:
        if NodoRaiz.hijoDer.valor == nodevalor:
            print("Valor encontrado")
        else:
            BuscarNodo(NodoRaiz.hijoDer, nodevalor)


def ValorMin(ArbolBinario):
    actual = ArbolBinario
    while (actual.hijoIzq is not None):
        actual = actual.hijoIzq
    return actual


def BorrarNodo(NodoRaiz, nodevalor):
    if NodoRaiz is None:
        return NodoRaiz
    if nodevalor < NodoRaiz.valor:
        NodoRaiz.hijoIzq = BorrarNodo(NodoRaiz.hijoIzq, nodevalor)
    elif nodevalor > NodoRaiz.valor:
        NodoRaiz.hijoDer = BorrarNodo(NodoRaiz.hijoDer, nodevalor)
    else:
        if NodoRaiz.hijoIzq is None:
            temp = NodoRaiz.hijoDer
            NodoRaiz = None
            return temp
        
        if NodoRaiz.hijoDer is None:
            temp = NodoRaiz.hijoIzq
            NodoRaiz = None
            return temp
        
        temp = ValorMin(NodoRaiz.hijoDer)
        NodoRaiz.valor = temp.valor 
        NodoRaiz.hijoDer = BorrarNodo(NodoRaiz.hijoDer, temp.valor)
    return NodoRaiz

def BorrarArbol(NodoRaiz):
    NodoRaiz.valor = None
    NodoRaiz.hijoIzq = None
    NodoRaiz.hijoDer = None
    return "Arbol eliminado"

arbolito = ArbolBinario(None)
AgregaNodo(arbolito, 7)
AgregaNodo(arbolito,2)
AgregaNodo(arbolito,1)
AgregaNodo(arbolito,3)
AgregaNodo(arbolito,5)
AgregaNodo(arbolito,4)
AgregaNodo(arbolito,8)
AgregaNodo(arbolito,6)
AgregaNodo(arbolito,9)
print("en postorden:")
RecorridoPostOrden(arbolito)
print("en orden:")
RecorridoEnOrden(arbolito)
print("en preorden:")
RecorridoPreOrden(arbolito)
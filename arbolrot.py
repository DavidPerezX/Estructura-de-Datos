import QueueLinkedList as queue
class ArbolRotado:
    def __init__(self, data):
        self.data = data
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

def Preorden(NodoRaiz):
    if not NodoRaiz:
        return
    print(NodoRaiz.data)
    Preorden(NodoRaiz.izquierdo)
    Preorden(NodoRaiz.derecho)

def Enorden(NodoRaiz):
    if not NodoRaiz:
        return
    Enorden(NodoRaiz.izquierdo)
    print(NodoRaiz.data)
    Enorden(NodoRaiz.derecho)

def Postorden(NodoRaiz):
    if not NodoRaiz:
        return
    Postorden(NodoRaiz.izquierdo)
    Postorden(NodoRaiz.derecho)
    print(NodoRaiz.data)

def BuscarNodo(NodoRaiz, ValordNodo):
    if NodoRaiz.data == ValordNodo:
        print("Valor encontrado")
    elif ValordNodo < NodoRaiz.data:
        if NodoRaiz.izquierdo.data == ValordNodo:
            print("Valor encontrado")
        else:
            BuscarNodo(NodoRaiz.izquierdo, ValordNodo)
    else:
        if NodoRaiz.derecho.data == ValordNodo:
            print("Valor encontrado")
        else:
            BuscarNodo(NodoRaiz.derecho, ValordNodo)

def getAltura(NodoRaiz):
    if not NodoRaiz:
        return 0
    return NodoRaiz.altura

def Rotaderecha(Nododesbalanceado):
    NuevaRAIZ = Nododesbalanceado.izquierdo
    Nododesbalanceado.izquierdo = Nododesbalanceado.izquierdo.derecho
    NuevaRAIZ.derecho = Nododesbalanceado
    Nododesbalanceado.altura = 1 + max(getAltura(Nododesbalanceado.izquierdo), getAltura(Nododesbalanceado.derecho))
    NuevaRAIZ.altura = 1 + max(getAltura(NuevaRAIZ.izquierdo), getAltura(NuevaRAIZ.derecho))
    return NuevaRAIZ

def Rotaizquierda(Nododesbalanceado):
    NuevaRAIZ = Nododesbalanceado.derecho
    Nododesbalanceado.derecho = Nododesbalanceado.derecho.izquierdo
    NuevaRAIZ.izquierdo = Nododesbalanceado
    Nododesbalanceado.altura = 1 + max(getAltura(Nododesbalanceado.izquierdo), getAltura(Nododesbalanceado.derecho))
    NuevaRAIZ.altura = 1 + max(getAltura(NuevaRAIZ.izquierdo), getAltura(NuevaRAIZ.derecho))
    return NuevaRAIZ

def getBalance(NodoRaiz):
    if not NodoRaiz:
        return 0
    return getAltura(NodoRaiz.izquierdo) - getAltura(NodoRaiz.derecho)

def InsertarNodo(NodoRaiz, ValordNodo):
    if not NodoRaiz:
        return ArbolRotado(ValordNodo)
    elif ValordNodo < NodoRaiz.data:
        NodoRaiz.izquierdo = InsertarNodo(NodoRaiz.izquierdo, ValordNodo)
    else:
        NodoRaiz.derecho = InsertarNodo(NodoRaiz.derecho, ValordNodo)
    
    NodoRaiz.altura = 1 + max(getAltura(NodoRaiz.izquierdo), getAltura(NodoRaiz.derecho))
    balance = getBalance(NodoRaiz)
    if balance > 1 and ValordNodo < NodoRaiz.izquierdo.data:
        return Rotaderecha(NodoRaiz)
    if balance > 1 and ValordNodo > NodoRaiz.izquierdo.data:
        NodoRaiz.izquierdo = Rotaizquierda(NodoRaiz.izquierdo)
        return Rotaderecha(NodoRaiz)
    if balance < -1 and ValordNodo > NodoRaiz.derecho.data:
        return Rotaizquierda(NodoRaiz)
    if balance < -1 and ValordNodo < NodoRaiz.derecho.data:
        NodoRaiz.derecho = Rotaderecha(NodoRaiz.derecho)
        return Rotaizquierda(NodoRaiz)
    return NodoRaiz

def getMinValueNode(NodoRaiz):
    if NodoRaiz is None or NodoRaiz.izquierdo is None:
        return NodoRaiz
    return getMinValueNode(NodoRaiz.izquierdo)

def BorrarNodo(NodoRaiz, ValordNodo):
    if not NodoRaiz:
        return NodoRaiz
    elif ValordNodo < NodoRaiz.data:
        NodoRaiz.izquierdo = BorrarNodo(NodoRaiz.izquierdo, ValordNodo)
    elif ValordNodo > NodoRaiz.data:
        NodoRaiz.derecho = BorrarNodo(NodoRaiz.derecho, ValordNodo)
    else:
        if NodoRaiz.izquierdo is None:
            temp = NodoRaiz.derecho
            NodoRaiz = None
            return temp
        elif NodoRaiz.derecho is None:
            temp = NodoRaiz.izquierdo
            NodoRaiz = None
            return temp
        temp = getMinValueNode(NodoRaiz.derecho)
        NodoRaiz.data = temp.data
        NodoRaiz.derecho = BorrarNodo(NodoRaiz.derecho, temp.data)
    balance = getBalance(NodoRaiz)
    if balance > 1 and getBalance(NodoRaiz.izquierdo) >= 0:
        return Rotaderecha(NodoRaiz)
    if balance < -1 and getBalance(NodoRaiz.derecho) <= 0:
        return Rotaizquierda(NodoRaiz)
    if balance > 1 and getBalance(NodoRaiz.izquierdo) < 0:
        NodoRaiz.izquierdo = Rotaizquierda(NodoRaiz.izquierdo)
        return Rotaderecha(NodoRaiz)
    if balance < -1 and getBalance(NodoRaiz.derecho) > 0:
        NodoRaiz.derecho = Rotaderecha(NodoRaiz.derecho)
        return Rotaizquierda(NodoRaiz)
    
    return NodoRaiz

def BorrarNodo(NodoRaiz):
    NodoRaiz.data = None
    NodoRaiz.izquierdo = None
    NodoRaiz.derecho = None
    return "Arbol eliminado"



NuevoArbol = ArbolRotado(5)
NuevoArbol = InsertarNodo(NuevoArbol, 5)
NuevoArbol = InsertarNodo(NuevoArbol, 15)
NuevoArbol = InsertarNodo(NuevoArbol, 20)
Postorden(NuevoArbol)

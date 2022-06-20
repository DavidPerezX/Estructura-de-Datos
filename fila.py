Fila=[]
tamaño=10


def full(fila,tamaño=10):
    if len(fila)==tamaño:
        return True
    return False

def empty(fila):
    if len(fila)==0:
        return True
    return False

def push(fila,elemento):
    if(full(fila,tamaño)):
        fila=fila+[elemento]
        print("La fila esta llena")
        return fila
    else:
        fila+=[elemento]
        return fila

def pop(fila):
    if(not empty(fila)):
        elemento=fila[0]
        fila=fila[1:len(fila)]
        return elemento,fila
    else:
        print("La fila esta vacía")
        return fila


print(empty(Fila))
Fila=push(Fila,"s")
Fila=push(Fila,"f")
Fila=push(Fila,"g")
Fila=push(Fila,"1")
Fila=push(Fila,"d")
Fila=push(Fila,"a")
print(Fila)
elemento,Fila=pop(Fila)
print(Fila)
print(full(Fila))
elemento,Fila=pop(Fila)
elemento,Fila=pop(Fila)
elemento,Fila=pop(Fila)
elemento,Fila=pop(Fila)
print(Fila)




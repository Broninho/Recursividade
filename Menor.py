
def Menor(lista):

    if(len(lista) == 0):
        print("ERRO!")
    elif len(lista) == 1:
        return (lista[0])

    M = Menor(lista[1:])

    if lista[0] < M:
        M = lista[0]

    return (M)

lista = [10,30,50,35,100,2]
print(Menor(lista))
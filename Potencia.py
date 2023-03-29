def Potencia(x,y):
    if y == 0:
        return 1
    else:
        return x * Potencia(x, y-1)

print(Potencia(10,2))
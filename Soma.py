def Soma(z):
    if z == 0:
        return 0
    else:
        return (z % 10) + Soma(z // 10)

print(Soma(250))
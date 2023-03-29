def MDC(y,z):
    while z != 0:
        r = y % z
        y = z
        z = r

    return y

def MMC(x,y):
    return x * (y / MDC(x,y))

print(MMC(10,2))
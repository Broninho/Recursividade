def MDC(y,z):
    while z != 0:
        r = y % z
        y = z
        z = r

    return y

print(MDC(100,5))
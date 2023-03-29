def fatorial(y):
    if y == 0 or y == 1:
        return 1
    else:
        return y * fatorial(y-1)


print(fatorial(5))
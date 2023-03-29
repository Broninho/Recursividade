def Fibo(y):
    if y == 1:
        return 0
    elif y == 2:
        return 1
    else:
        return Fibo(y-1) + Fibo(y-2)

print(Fibo(10))
import math

a = float(input("Digite o primeiro número da equação: "))
b = float(input("Digite o segundo número da equação: "))
c = float(input("Digite o terceiro número da equação: "))
delta = b ** 2 - 4 * a * c

def calcula(a, b, c):
    if (delta < 0):
        print("esta equação não possui raízes reais")
    elif delta == 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        print("a raiz desta equação é", raiz1)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        if (raiz1 > raiz2):
            print("as raízes da equação são", raiz2, "e", raiz1)
        elif (raiz2 > raiz1):
            print("as raízes da equação são", raiz1, "e", raiz2)


calcula(a, b, c)
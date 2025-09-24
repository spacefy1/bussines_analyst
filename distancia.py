import math

x1 = float(input("Digite o primeiro número da equação: "))
x2 = float(input("Digite o segundo número da equação: "))
dif1 = x1 - x2

y1 = float(input("Digite o terceiro número da equação: "))
y2 = float(input("Digite o quarto número da equação: "))
dif2 = y1 - y2

def distancia(x1, x2, y1, y2):
    elevado = dif1 ** 2
    elevado2 = dif2 ** 2
    d1 = elevado + elevado2
    d2 = math.sqrt(d1)

    if (d2 >= 10):
        print("longe")
    else:
        print("perto")

    return d2

distancia(x1, x2, y1, y2)


n1 = int(input("Digite o valor de n: "))

def impar(n1):
    n2 = 1
    while n1 != 0:
        if n2 % 2 != 0:
            print(n2)
        n2 += 2

        n1 -= 1

impar(n1)
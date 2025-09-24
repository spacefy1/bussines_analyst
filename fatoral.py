def fatorial_while(n):
    if n == 0 or n == 1:
        return 1

    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1

    return resultado


n1 = int(input("Digite o valor de n: "))


print(fatorial_while(n1))
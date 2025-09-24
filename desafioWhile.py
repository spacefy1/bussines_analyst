x10 = int(input("Digite um numero: "))

def somar(x10):
    soma = 0

    while x10 != 0:
        digito = x10 % 10
        soma += digito
        x10 //= 10

    print(soma)


somar(x10)
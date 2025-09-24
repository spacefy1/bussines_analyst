n1 = int(input("Digite um número inteiro: "))

def rep(n1):
    numero_adjacente = False
    num = 0
    if n1 < 10:
        print("não")
    else:
        while n1 >= 10:
            n3 = n1 % 10
            n1 //= 10
            num = n1 % 10
            if n3 == num:
                numero_adjacente = True
                break


    if numero_adjacente:
        print("sim")
    else:
        print("não")

rep(n1)
n1 = int(input("Digite um número inteiro: "))



def primo(n1):

    num = 2
    if n1 == 2:
        eprimo
    else:
        while n1 > num:
            if n1 % num == 0:
               eprimo = False
               break
            elif n1 % 2 == 0 and n1 > 2:
                eprimo = False
            num += 1

        return "primo"

if primo(n1):
    print ("primo")
else:
    print("não primo")


def computador_escolhe_jogada (n, m):
    x = n % (m+1)
    #para chamar uma funçao apos a outra NAO posso chamar
    #jogador_escolhe_jogada aqui, pois nao devolvem nada

    #while(n > 0): --> devo implementar o while na FUNCAO
    #partida

    # se o resto da divisao NAO for 0, o computador tira
    # o MAXIMO de m :_)

    if x != 0:
        n -= m
        print(f"O computador retirou {x} peça")
        return x
    else:
        n -= m
        print(f"O computador retirou {x} peça")
        return m

def usuario_escolhe_jogada(n, m):
    #este laço devolve

    while True:
        try:
            x = int(input("\nQuantas peças você vai tirar? "))

            if x >= 1 and x <= m and x <= n:
                return x  # Retorna o numero de pecas TIRADAS
            else:
                print("Oops! Jogada inválida! Tente de novo.")

        except ValueError:
            print("Oops! Jogada inválida! Tente de novo.")

def partida():
    #sao escolhidas apenas uma vez

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1)) == 0:
        print("\nVocê começa!")
        turno = 'jogador'
    else:
        print("\nComputador começa!")
        turno = 'computador'

    while n > 0:
        if turno == 'jogador':
            # Chame a função do jogador
            pecas_tiradas = usuario_escolhe_jogada (n, m)
            n -= pecas_tiradas

            if pecas_tiradas > 1:
                print(f"Você retirou {pecas_tiradas} peças.")
            else:
                print(f"Você retirou uma peça.")

            if n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            elif n == 1:
                print(f"Agora restam uma peça no tabuleiro.\n")
            else:
                print("Fim do jogo! Você ganhou!")
            turno = 'computador'  # Passa o turno para o computador
        else:
            pecas_tiradas = computador_escolhe_jogada(n, m)
            n -= pecas_tiradas
            if pecas_tiradas > 1:
                print(f"Computador retirou {pecas_tiradas} peças.")
            else:
                print(f"Computador retirou uma peça.")


            if n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            elif n == 1:
                print(f"Agora restam uma peça no tabuleiro.\n")
            else:
                print("Fim do jogo! O computador ganhou!\n")
            turno = 'jogador'

def campeonato():
    flag = 0
    for i in range(1, 3, 1):
        print(f"**** Rodada {i} ****")
        partida()
        if i == 3:
            flag = 1

    if flag == 1:
        print("**** Final do campeonato! ****")
        # nao consegui uma forma de solucionar as vitorias e derrotas de cada,
        # porem presumi que o computador sempre ganha :)

        print("\nPlacar: Você 0 X 3 Computador")


def jogar():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    escolha = int(input("\n1 - para jogar uma partida isolada \n2- para jogar um campeonato "))

    print("\n")

    # variaveis de escolha para começar o jogo
    if escolha == 1:
        print("Voce escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Voce escolheu um campeonato!")
        campeonato()

    else:
        print("Entrada errada!")

jogar()
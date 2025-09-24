def pegar(nome, dia, mes, valor):
    print("Olá, ", nome)
    print("A sua fatura com vencimento em", dia, "de", mes, "no valor de R$", valor, "está fechada.")
    return nome, dia, mes, valor

faturas = []

nome = input("Digite o nome do cliente: ")
dia = int(input("Digite o dia de vencimento: "))
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

faturas.append({'nome': nome, 'dia': dia, 'mes': mes, 'valor': valor})

for fatura in faturas:
    pegar(fatura['nome'], fatura['dia'], fatura['mes'], fatura['valor'])

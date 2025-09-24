nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

def media(nota1, nota2, nota3, nota4):
    mediaAritemetica = (nota1 + nota2 + nota3 + nota4) / 4
    return mediaAritemetica

print("A média aritmética é:", media(nota1, nota2, nota3, nota4))
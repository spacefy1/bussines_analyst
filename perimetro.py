lado = int(input("Digite o valor do lado: "))

def perimetro(lado):
    x = lado * 4
    return x

def area(lado):
    y = lado ** 2
    return y

print("perímetro:", perimetro(lado), "area:", area(lado))
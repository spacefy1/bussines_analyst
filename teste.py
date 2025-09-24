def fatorial(n):
    fat = 1
    while (n >1):
        fat = fat * n
        n = n - 1
    return fat

def num_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def testa_fat():
    o = 50000
    while True:
        if (num_binomial(9, 5) == o):
            print(f"O teste de {o} deu certo!")

        o -= 500

num_binomial(9, 5)
testa_fat()
from math import sqrt

def ehPrimo(k):
    limit = int(sqrt(k)) + 1

    if(k <= 1):
        return False
    elif (k == 2):
        return True
    elif (k % 2 != 0):
        for i in range(3, limit, 2):
            if (k % i == 0):
                return False

        return True


def maior_primo(maior_primo):
    if (maior_primo <= 2):
        print(2)

    for i in range(maior_primo, 1, -1):
        if ehPrimo(i):
            return i




def test_primo():
    assert maior_primo(3) == 3
def maximo(n, k):
    if(n > k):
        print(n)
        return n
    elif(k > n):
        print(k)
        return k
    else:
        print(n)
        return n

def test_maximo():
    assert maximo(9, 2) == 9
    assert maximo(0, -1) == 0
    assert maximo(1, 1) == 1
    assert maximo(3, 4) == 4

maximo(3, 4)
maximo(0, -1)
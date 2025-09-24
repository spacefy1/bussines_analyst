def maximo(n1, n2, n3):
    if (n1 >= n2 and n1 >= n3):
        return n1
    elif (n2 >= n1 and n2 >= n3):
        return n2
    elif(n3 >= n1 and n3 >= n2):
        return n3

def test_maximo():
    assert maximo(1, 4 , 9) == 9
    assert maximo(62, 13, 24) == 62

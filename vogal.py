def vogal(text):

    if(text == "a" or text == "e" or text == "i" or text == "o" or text == "u"):
        return True
    else:
        return False


def test_vogal():
    assert vogal("a") == True
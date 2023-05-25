from numb3rs import validate

def test_ipv4():
    assert validate('01.102.103.104') == True


def test_invalid():
    assert validate('275.3.6.28') == False

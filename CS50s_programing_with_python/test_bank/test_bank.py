from bank import value

def test_hello():
    assert value('hello') == 0

def test_h():
    assert value('hey') ==20

def test_others():
    assert value('cs50') == 100

def test_upper_hello():
    assert value('Hello') == 0

def test_upper_h():
    assert value('Hey') ==20

def test_upper_others():
    assert value('Cs50') == 100
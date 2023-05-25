from twttr import shorten

def test_shorten():
    assert shorten('hello') == 'hll'
    assert shorten('my name is tiago') == 'my nm s tg'
    assert shorten('this is cs50') == 'ths s cs50'
    assert shorten('this is python') == 'ths s pythn'

def test_uppercase():
    assert shorten("Harvard") == "Hrvrd"
    assert shorten("TIAGO") == "TG"

def test_numb():
    assert shorten('0') == '0'

def test_pontuation():
    assert shorten(',') == ','
from plates import is_valid

def test_size():
    assert is_valid('OUTATIME') == False

def test_chars():
    assert is_valid('PI3.14') == False

def test_start():
    assert is_valid('44AH') == False

def test_sequence():
    assert is_valid('CS50P') == False

def test_frist_number():
    assert is_valid('ABC02') == False

def test_numbers():
    assert is_valid('123456') == False
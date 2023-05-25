from um import count

def test_um():
    assert count("um") == 1

def test_nospace():
    assert count("umum") == 0

def test_upper():
    assert count("UM um Um") == 3
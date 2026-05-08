from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 6) == 4


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 5) == 2.0

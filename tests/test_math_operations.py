
def add(a: int, b:int) -> int:
    return a + b

def subtract(a: int, b:int) -> int:
    return a - b

def multiply(a: int, b:int) -> int:
    return a * b

def divide(a: int, b:int) -> int:
    return a // b


#tests
def test_add() -> None:
    assert add(1, 2) == 4
def test_subtract() -> None:
    assert subtract(5,2) == 3
def test_multiply() -> None:
    assert multiply(10,10) == 100
def test_divide() -> None:
    assert divide(25,100) == 0
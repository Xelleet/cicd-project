from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 8, "Ошибка в сложении"

def test_subtract():
    assert subtract(5, 2) == 3, "Ошибка в вычитании"

def test_multiply():
    assert multiply(2, 3) == 6, "Ошибка в умножении"

def test_divide():
    assert divide(6, 2) == 3, "Ошибка в делении"

print("✅ Все тесты прошли!")
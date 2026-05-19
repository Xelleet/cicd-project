from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5, "Сложение работает неправильно"


def test_subtract():
    assert subtract(5, 2) == 3, "Вычитание работает неправильно"


def test_multiply():
    assert multiply(2, 3) == 6, "Умножение работает неправильно"


def test_divide():
    assert divide(6, 2) == 3, "Деление работает неправильно"


if __name__ == "__main__":
    # Запускаем все тесты
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

    print("✅ Все тесты прошли успешно!")
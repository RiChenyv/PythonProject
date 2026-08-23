def test_func(computer):
    result = computer(1, 2)
    print(type(computer))
    print(result)


def computer(a, b):
    return a + b


test_func(computer)

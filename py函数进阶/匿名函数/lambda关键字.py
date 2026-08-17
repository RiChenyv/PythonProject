# lambda 传入参数:函数体(一行代码)
def test_func(computer):
    result = computer(1, 2)
    print(result)


test_func(lambda x, y: x + y)
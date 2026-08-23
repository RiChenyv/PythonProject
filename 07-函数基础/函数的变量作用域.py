# 主要分为局部变量和全局变量
def testA():
    """
    num为局部变量，只能在函数内使用
    :return: num
    """
    num = 100
    return num


def testB():
    """
    在函数中调用全局变量test_a
    :return: num的值(test_a)
    """
    return test_a


test_a = testA()
# test_a为全局变量
b = testB()
print(b)
print("\n")
print(test_a)
# print(num) 会出现以下报错
"""
Traceback (most recent call last):
  File "D:\PythonProject\07-函数基础\函数的变量作用域.py", line 12, in <module>
    print(num)
          ^^^
NameError: name 'num' is not defined. Did you mean: 'sum'?
"""

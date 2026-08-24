# 对形参进行类型注解
def add(x: int, y: int):
    return x + y


# 对返回值进行类型注解
def func(data: list) -> list:
    return data


"""同理，在函数和方法中型注解也仅起到标注作用，是提示性作用，并非直接限制变量的类型的决定性作用"""
all = add(1, 2)
print(all)
print(func(all))
print(type(func(all)))

def say_hello():
    print('hello')


def add(x, y):
    print(f"{x}+{y}={x + y}")
    return x + y


say_hello()
a = add(10, 20)
print(a)

def print_b():
    global number
    number = 100
    return number

def print_c():
    global number
    number = 200
    return number

number = 5
b = number
print(b)
a = print_b()
print(a)
number = 10
a = number
print(a)

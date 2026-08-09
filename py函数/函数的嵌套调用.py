def print_a():
    print("-----a-----")


def print_b():
    print("-----b-----")
    print_a()


def print_c():
    print("-----c-----")
    print_a()
    print_b()

print_a()
print("——————————————————————————————————————")
print_b()
print("——————————————————————————————————————")
print_c()

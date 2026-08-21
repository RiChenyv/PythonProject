def funco1():
    print("1")
    1 / 0
    print("2")


def funco2():
    print("3")
    funco1()
    print("4")


def main():
    try:
        funco2()
    except Exception as e:
        print(e)


main()
